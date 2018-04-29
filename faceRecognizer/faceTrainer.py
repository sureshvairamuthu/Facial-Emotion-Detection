import cv2,os
import numpy as np
#from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector= cv2.CascadeClassifier("../venv/lib/python3.5/site-packages/cv2/data/haarcascade_frontalface_default.xml");

def getImagesAndLabels(path):
	#get the path of all the files in the folder
	imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
	#create empth face list
	faceSamples=[]
	#create empty ID list
	Ids=[]
	#now looping through all the image paths and loading the Ids and the images
	for imagePath in imagePaths:
		#loading the image and converting it to gray scale
		#image = #Image.open(imagePath).convert('L')
		image= cv2.imread(imagePath)
		pilImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		#Now we are converting the PIL image into numpy array
		imageNp=np.array(pilImage,'uint8')
		#getting the Id from the image
		Id=int(os.path.split(imagePath)[-1].split(".")[1])
		# extract the face from the training image sample
		faces=detector.detectMultiScale(imageNp)
		#If a face is there then append that in the list as well as Id of it
	for (x,y,w,h) in faces:
		faceSamples.append(imageNp[y:y+h,x:x+w])
		Ids.append(Id)
	return faceSamples,Ids


faces,Ids = getImagesAndLabels('/home/sureshvairamuthu/Facial-Emotion-Detection/faceRecognizer/faceDataset')
recognizer.train(faces, np.array(Ids))
recognizer.save('/home/sureshvairamuthu/Facial-Emotion-Detection/faceRecognizer/faceTrainer/faceTrainer.yml')