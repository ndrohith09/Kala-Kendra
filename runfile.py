#NOTE:  This must be the first call in order to work properly!
import os 
# cwd = os.getcwd() 
# print("cwd" , cwd)
# print(os.listdir(cwd))
# abs_path = cwd+ '/app/DeOldify' 
# # abs_path = '/home/rohithnd/zorin/Code/artist asylum/artist/app/DeOldify'
# os.chdir(abs_path)
# # print(os.getcwd())

import PIL
from deoldify import device
from deoldify.device_id import DeviceId
from moviepy.editor import *

print(device.set(device=DeviceId.GPU0))
import torch
if not torch.cuda.is_available():
    print('GPU not available.')

from deoldify.visualize import *
from PIL import Image
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?") 

def colorize(source_url, render_factor=35, watermarked=False):
    print("Colorizing image:", source_url)
    colorizer = get_image_colorizer(artistic=True)

    if source_url is not None and source_url !='':
        image_path = colorizer.plot_transformed_image_from_url(url=source_url, render_factor=render_factor, compare=True, watermarked=watermarked)
        img = show_image_in_notebook(image_path) 
        print("image path" , image_path)
        im = Image.open(image_path , 'r')
        im.save("static/img/products/output.jpg" , "JPEG")
        print("im" , im , type(im))         
        # im.show() 
        return image_path
    else:
        print('Provide an image url and try again.')

# source_url = 'https://images.unsplash.com/photo-1578393098337-5594cce112da?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=617&q=80'  
# colorize(source_url)

def colorize_video(source_url, render_factor=35, watermarked=False):
    print("Colorizing image:", source_url)
    colorizer = get_video_colorizer()

    if source_url is not None and source_url !='':
        render_factor = 21  #@param {type: "slider", min: 5, max: 40}
        watermarked = False #@param {type:"boolean"}

        if source_url is not None and source_url !='':
            # video_path = colorizer.colorize_from_url(source_url, 'video.mp4', render_factor, watermarked=watermarked)
            video_path = colorizer.colorize_from_file_name(source_url)
            show_video_in_notebook(video_path) 
 
            clip = VideoFileClip(video_path)   # load video
            clip.write_videofile("static/video/video.mp4") 
            return video_path

        else:
            print('Provide a video url and try again.')
    else:
        print('Provide an video url and try again.')

# colorize_video('demo.mp4')
# colorize_video('https://www.dropbox.com/s/wechbxqpyd5gmu7/new_york_city_bw.mp4?dl=0')