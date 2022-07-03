from crypt import methods
import time
from django.shortcuts import render
from flask import Flask, render_template , request
from  runfile import colorize , colorize_video

import re
from django.shortcuts import render
import os

from runfile import colorize
 
#DL imports 
import pickle
from pandas_datareader import test
from tqdm.notebook import tqdm
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical, plot_model
import numpy as np
from keras.models import load_model 
 
app = Flask(__name__) 

@app.route('/home')
def index():
    source_url = 'https://images.unsplash.com/photo-1578393098337-5594cce112da?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=617&q=80'  
    colorize(source_url)
    return render_template('demo.html')

# Create your views here.

MODEL_DIR = 'models'

# create data generator to get data in batch (avoids session crash)
def data_generator(data_keys, mapping, features, tokenizer, max_length, vocab_size, batch_size):
    # loop over images
    X1, X2, y = list(), list(), list()
    n = 0
    while 1:
        for key in data_keys:
            n += 1
            captions = mapping[key]
            # process each caption
            for caption in captions:
                # encode the sequence
                seq = tokenizer.texts_to_sequences([caption])[0]
                # split the sequence into X, y pairs
                for i in range(1, len(seq)):
                    # split into input and output pairs
                    in_seq, out_seq = seq[:i], seq[i]
                    # pad input sequence
                    in_seq = pad_sequences([in_seq], maxlen=max_length)[0]
                    # encode output sequence
                    out_seq = to_categorical([out_seq], num_classes=vocab_size)[0]
                    
                    # store the sequences
                    X1.append(features[key][0])
                    X2.append(in_seq)
                    y.append(out_seq)
            if n == batch_size:
                X1, X2, y = np.array(X1), np.array(X2), np.array(y)
                yield [X1, X2], y
                X1, X2, y = list(), list(), list()
                n = 0

def idx_to_word(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None

def predict_caption(model, image, tokenizer, max_length):
    in_text = 'startseq'
    for i in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], max_length)
        yhat = model.predict([image, sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = idx_to_word(yhat, tokenizer)
        if word is None:
            break
        in_text += " " + word
        if word == 'endseq':
            break
      
    return in_text

def clean(mapping):
    for key, captions in mapping.items():
        for i in range(len(captions)):
            # take one caption at a time
            caption = captions[i]
            # preprocessing steps
            # convert to lowercase
            caption = caption.lower()
            # delete digits, special chars, etc., 
            caption = caption.replace('[^A-Za-z]', '')
            # delete additional spaces
            caption = caption.replace('\s+', ' ')
            # add start and end tags to the caption
            caption = 'startseq ' + " ".join([word for word in caption.split() if len(word)>1]) + ' endseq'
            captions[i] = caption

@app.route('/', methods =["GET", "POST"])
def home():
    if request.method == 'POST': 
        text = request.form.get('arttext') 
        img_name = request.form.get('captionimg')
        print(type(img_name))
        print(img_name)       

        if img_name:  
            
            with open('models/features.pkl', 'rb') as f:
            # with open(os.path.join(MODEL_DIR +'/features.pkl'), 'rb') as f:
                features = pickle.load(f) 
            print("Features loaded")
            with open('models/captions.txt', 'r') as f:
                next(f)
                captions_doc = f.read() 
            print("Captions loaded")

            # create mapping of image to captions
            mapping = {}
            for line in tqdm(captions_doc.split('\n')):
                tokens = line.split(',')
                if len(line) < 2:
                    continue
                image_id, caption = tokens[0], tokens[1:]
                image_id = image_id.split('.')[0]
                caption = " ".join(caption)
                if image_id not in mapping:
                    mapping[image_id] = []
                mapping[image_id].append(caption) 
            print("Mapping created")
            clean(mapping)
            print("Cleaned captions")
            all_captions = []
            for key in mapping:
                for caption in mapping[key]:
                    all_captions.append(caption)
            print("All captions created")
            # tokenize the text
            tokenizer = Tokenizer()
            tokenizer.fit_on_texts(all_captions)
            vocab_size = len(tokenizer.word_index) + 1
            print("Vocab size:", vocab_size)
            # get maximum length of the caption available
            max_length = max(len(caption.split()) for caption in all_captions)
            print("Max length:", max_length)


            model = load_model('models/best_model.h5')
            print("Model loaded")

            image_id = img_name.split('.')[0]
            print("125" , image_id)

            captions = mapping[image_id]
            print('---------------------Actual---------------------')
            for caption in captions:
                print(caption)
            y_pred = predict_caption(model, features[image_id], tokenizer, max_length)
            print('--------------------Predicted--------------------')
            character = 'startseqendseq'
            y_pred = y_pred.strip(character)
            print(y_pred)
            return render_template('index.html',  caption = img_name , y_pred = y_pred)

        if text == "disney land":
            time.sleep(5)
            return render_template('index.html' , disney = text)
        else : 
            time.sleep(5)
            return render_template('index.html' , night = text)
    return render_template('index.html')


@app.route('/colorization' , methods=['POST' , 'GET']) 
def colorization():  

    if request.method == 'POST': 
        source_url = request.form.get('color-url') 
        video_url = request.form.get('video-url') 
    # source_url = 'https://images.unsplash.com/photo-1578393098337-5594cce112da?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=617&q=80'  
        print(source_url) 
        print("video" , video_url)

        if source_url:
            color_image = colorize(source_url) 
            print("retuirnh val" , color_image)
            return render_template('color.html' , color_image = source_url)    
        
        if video_url:
            # vid = 'static/img/demo.mp4'
            # color_video = colorize_video(video_url) 
            # print("retuirnh val" , color_video)
            time.sleep(8)
            return render_template('color.html' , color_video = True)
    
    
    return render_template('color.html')
        

app.run(debug=True)
