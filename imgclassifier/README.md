# PictureClassifier
This part of the project is able to classify an image and assign it a label. It uses a deep convolutional neural network (CNN). In order to use the system, first we must process the input images and then train the network. We will take the following steps:
1. **Prepare the images**. All the images should be under the directory 'images'. Inside this directory we will have one directory per object we want the CNN to recognize. The name of the directory will be the label the CNN will return when recognizing a picture. For preparing the images, make sure you all the images that you want to use in the directory 'images' and execute: 
```Rscript prepare_images.R```
