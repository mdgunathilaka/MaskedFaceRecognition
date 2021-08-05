# MaskedFaceRecognition

##project description

This is the repository for my semster 5 Industrial Computer Engineering project. Theis project focuses on building an accurate facial recognition system which can identify people using thier facial features while they are wearing masks. Then that system will be used as a customer identification system for a resturant. It will help with provinfing customer's previous meal or privious table.
There are such systems already in the market but since the covid pandemic, it is known that most of those systems could not identify masked people.

##Data

Since the facial recognition is done by using only the parts which are not covered by masks, that leaves only the top 40% of a face. And to make the model acuurate, a large number of faces needed. These are publicly available face datasets I intend to use.

- LFW dataset
Labelled Faces in the Wild dataset. This contains more than 13,000 images of faces. Avalable on http://vis-www.cs.umass.edu/lfw/

- YouTube Faces
YouTube Faces dataset is a database of face videos designed for studyning the problem of unconstrained face recognition in videos. This contains 3,425 videos downloaded from youtube. Available on https://www.cs.tau.ac.il/~wolf/ytfaces/

##Proposed Architecture

The system will have a detector device which consists of a raspberry pi and a camera, a face recognition models that runs on a cloud, and a client app to get the customer details.

![image](https://user-images.githubusercontent.com/59095109/128291406-abe10075-319e-43a2-a0cb-24685a5822c1.png)
