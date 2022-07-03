## Inspiration
- With the rise of AI, it becomes easier for artists to express themselves without having to go through the process of creating an artwork.
- Artificial intelligence has the ability to consistently learn from past experiences and adapt to changes, making it the perfect candidate for eventually generating meaningful captions.
- These factors make it easier for users to interact comfortably when the application supports voice.

## What it does
### **AI Art generator**
- A single line of text can be used to generate art. The model will generate the art based on the text provided.
- You are taken to the art generator space after giving the voice command `art generator` .
- Just talk about the art you need to produce. For example `generate art for city at night` .

![AI art](https://firebasestorage.googleapis.com/v0/b/react-firechat-ae4bf.appspot.com/o/as-11.png?alt=media&token=3b8f1c45-7898-461d-a5a1-ead91ddb5113) 

- The output will be generated for the desired input.
![AI Art generator](https://firebasestorage.googleapis.com/v0/b/react-firechat-ae4bf.appspot.com/o/as-12.png?alt=media&token=47932b81-4824-4f04-9e71-7cf8492e8e85)

### **AI Caption generator**
- The AI-based caption generator can generate captions for your images within seconds.
- Giving the voice command `caption generator` will bring you to the art generator area.
- When you say the command `upload caption file` , a dialog box appears, allowing you to choose the image for which you need to create a caption.
- Once the image is uploaded you can see the preview of the uploaded image below.
- The caption for your image will now be generated when you speak on the `generate caption` or by pressing the `generate button`.

![AI caption generator](https://firebasestorage.googleapis.com/v0/b/react-firechat-ae4bf.appspot.com/o/as-13.png?alt=media&token=34b9ec4c-d00d-470b-84ca-0cc684120776)

- Once the caption has been created, use the command `speak caption` or by clicking on the `speak button` to have the AI read out your generated caption.

![AI caption generator](https://firebasestorage.googleapis.com/v0/b/react-firechat-ae4bf.appspot.com/o/as-14.png?alt=media&token=27edb6c1-75c5-4f66-9312-66f675d791cd)

### **Color Restoration**
- For restoring color to your image , upload the image url of the specified image and press generate button. 

![image color](https://firebasestorage.googleapis.com/v0/b/react-firechat-ae4bf.appspot.com/o/as-7.png?alt=media&token=64fca4e4-2318-41c4-80a4-dea48dc60a49)
![image color](https://firebasestorage.googleapis.com/v0/b/react-firechat-ae4bf.appspot.com/o/as-8.png?alt=media&token=cbb46d98-ad57-46e2-a3d6-f848f4fd16f7)

- For restoring color to your video , upload the video url of the specified video and press generate button. 

![video color](https://firebasestorage.googleapis.com/v0/b/react-firechat-ae4bf.appspot.com/o/as-9.png?alt=media&token=a419400b-fbe7-41aa-b9fd-918b578538d3)

![video color](https://firebasestorage.googleapis.com/v0/b/react-firechat-ae4bf.appspot.com/o/as-10.png?alt=media&token=6598d584-7196-416f-937f-10659f642a90)

## How we built it
- The AI art generator was created using Generative adversarial network and Imagenet 16384.
- The AI caption generator was developed using LSTM and was trained on the flickr dataset. 
- The color restoration was created based on DeOldify model.
- HTML, CSS, and Bootstrap were used to create the user interface.
- We used Django as our backend to integrate our Deep learning model with the UI.
-  `Alan AI API` were utilised to implement voice interaction in the application.

## Challenges we ran into
- Deep learning model training required a significant amount of time and computation power.
- It was difficult to integrate our deep learning model with the user interface.
- Improving the model's accuracy was an aesthetic taste.
- Integrating color restoration domain in the application was the toughest part. 
- Making the application more interactive by Voice was a challenging part. It took us some time to understand and work on with Assembly AI Api and Alan AI Api.

## Accomplishments that we're proud of
- We were able to create an amazing model that can generate art , captions for images and restore color for images and videos. 
- Possibly developing a web application and incorporating this model was incredible.
- Making the application more interactive with voice command was an interesting part of our application.
 
## What we learned
We discovered a lot about Deep Learning models and their applications. We got some knowledge on MLOps. We most likely learned more about GANs and LSTM. We worked on with Api's for interacting with the web application.

## What's next for Kala Kendra
- Should try to reduce the process time for each request. 
- Improve the AI art generator with more options which can make the art generation flexible.
- Working on to improve the accuracy of the models.
- Should include more features in voice interaction.
- Make file upload field available for color restoration application. 
