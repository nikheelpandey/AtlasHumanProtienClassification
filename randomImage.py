import numpy as np 
from uuid import uuid4
import cv2
import pandas as pd 
"""
Sample imagae dataset and sample label.  
"""
saving_path = "../train/" 

def makeFakeLabel(): return np.random.randint(2,size=28)

def randomImage():

	R = np.random.randint(255, size=(256,256)).astype('uint8')
	G = np.random.randint(255, size=(256,256)).astype('uint8')
	B = np.random.randint(255, size=(256,256)).astype('uint8')
	Y = np.random.randint(255, size=(256,256)).astype('uint8')

	return(R,G,B,Y)


dictt = []
ID = []
for i in range(50):
	id = str(uuid4())
	R,G,B,Y = randomImage()
	cv2.imwrite(saving_path+id+"_red.png",R)
	cv2.imwrite(saving_path+id+"_blue.png",B)
	cv2.imwrite(saving_path+id+"_green.png",G)
	cv2.imwrite(saving_path+id+"_yellow.png",Y)

	label=makeFakeLabel()
	label = np.arange(28)[label>0]
	label = ' '.join(str(l) for l in label)
	dictt.append(label)
	ID.append(id)

df = pd.DataFrame({"id":ID,"label":dictt})
df.to_csv("train.csv",index=False)

