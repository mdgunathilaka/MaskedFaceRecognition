import numpy as np
import json
from PIL import Image

data1=[]
data2=[]
labels=[]

f = open("mask_pairs.txt", "r")
for line in f:
    img1, img2, label = map(str,line.split())
    image1 = Image.open(img1 + '.jpeg')
    image2 = Image.open(img2 + '.jpeg')
    data1.append(np.asarray(image1))
    data2.append(np.asarray(image2))
    labels.append(label)
    #print(img2)

dataar1 = np.array(data1)
dataar2 = np.array(data2)
labelar = np.array(label)

'''
def save_json(self, data, name):
    with open(name + ".json", 'w') as outfile:
        json.dump(data.tolist(), outfile)
'''