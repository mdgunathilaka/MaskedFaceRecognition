# MaskedFaceRecognition

## project description

This is the repository for my semster 5 Industrial Computer Engineering project. Theis project focuses on building an accurate facial recognition system which can identify people using thier facial features while they are wearing masks. Then that system will be used as a customer identification system for a resturant. It will help with provinfing customer's previous meal or privious table.
There are such systems already in the market but since the covid pandemic, it is known that most of those systems could not identify masked people.

## Data

Since the facial recognition is done by using only the parts which are not covered by masks, that leaves only the top 40% of a face. And to make the model acuurate, a large number of faces needed. These are publicly available face datasets I intend to use.

- LFW dataset
Labelled Faces in the Wild dataset. This contains more than 13,000 images of faces. Avalable on http://vis-www.cs.umass.edu/lfw/

- YouTube Faces
YouTube Faces dataset is a database of face videos designed for studyning the problem of unconstrained face recognition in videos. This contains 3,425 videos downloaded from youtube. Available on https://www.cs.tau.ac.il/~wolf/ytfaces/

To generate synthetic masks on faces, I intend follow the approach by Dr.Sachith. https://github.com/sachith500/MaskedFaceRepresentation

## Proposed Architecture

The system will have a detector device which consists of a raspberry pi and a camera, a face recognition models that runs on a cloud, and a client app to get the customer details.

![image](https://user-images.githubusercontent.com/59095109/128291406-abe10075-319e-43a2-a0cb-24685a5822c1.png)

The system will work in a producer consumer pattern. So the detector device will capture a face and send it to the server, then it will not wait for result to capture the next frame. With this it can capture more frames and provide good quality images. And the recognition server can have a very deep model as well. Currently, the idea is to build it using pretrained vgg-face model as a base.

## Final Demonstration (Planned)

1. Face recognition model (uploaded in a server)
![image](https://user-images.githubusercontent.com/59095109/128292341-fa6e3a54-332b-484c-8998-3ba01edbb431.png)

2. Raspberry pi integrated with a camera to detect and send images to server
![image](https://user-images.githubusercontent.com/59095109/128292485-f5f23f02-7eee-4ffe-a317-581b0dc5ac13.png)

3. App to receive information about the detected people
![image](https://user-images.githubusercontent.com/59095109/128292566-e47ce774-7db2-4455-b257-c38796655050.png)

## Components and technologies

1. Raspberry Pi 3b+
2. Camera (Pi camera v1.3)
3. TensorFlow and OpenCV
4. Google Cloud, Docker and Flutter

## Related Works

1. https://www.researchgate.net/publication/342757061_Efficient_Masked_Face_Recognition_Method_during_the_COVID-19_Pandemic


## 2021.10 Updates

- Using cropped images is less efficient. Moved onto detect full face. Used the mediapipe library's MultiFaceDetector. It can detect both masked and unmasked faces with a good accuracy.
- For the training purpose, finding a big dataset with labeled masked faces was not possible.
- Generated simulated masks for the LFW dataset and created masked faces.
- Currently Builing a VGG-face based siamese network for recognizing faces.
- For the training, image pairs are needed. Creating a list of images for the purpose and then those images will be turned into np arrays and stacked together to build the dataset.


