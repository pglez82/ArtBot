# PictureClassifier
This part of the project is able to classify an image and assign it a label. It uses a deep convolutional neural network (CNN). In order to use the system, first we must process the input images and then train the network. We will take the following steps:
1. **Data augmentation**. All the images should be under the directory 'images'. Inside this directory we will have one directory per object we want the CNN to recognize. The name of the directory will be the label the CNN will return when recognizing a picture. In this step we will create multiple versions of the same images, making variations in contrast, rotation, etc. This script will also make the images square (required by the CNN). Make sure you all the images that you want to use in the directory 'images' and execute: ```Rscript prepare_images.R```
2. **Pack the images**. In order to train the CNN the images must be packed. Just run the script ```./pack_images.sh```. It will create a few files in the same directory.
3. **Train the network**. In this step we will take all the packaged pictures and we will feed them to the network. In this process the network will adjusts its weights in order to learn how to recognize this images. This step can take a long time. The script for training the network is: ```finetuneCNN.sh```
4. **Test the trained network**. At this point we already have the network trained. The class ```img_classifier.py``` contains a class that allows you to classify a new image. Use the following code in order to test the system:
	```python
	from img_classifier import PictureClassifier
	c = PictureClassifier()
	probs=c.predict('images/carreno/carreno.jpg')
	print probs
	```
