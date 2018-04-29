import cv2
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('/home/sureshvairamuthu/Facial-Emotion-Detection/faceRecognizer/faceTrainer/faceTrainer.yml')
haar_face_cascade = cv2.CascadeClassifier('../venv/lib/python3.5/site-packages/cv2/data/haarcascade_frontalface_default.xml')
Id=0

cam = cv2.VideoCapture(0)


while True:
	ret, im =cam.read()

	gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

	faces = haar_face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5);

	for(x,y,w,h) in faces:
		cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
		Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
		if(conf<50):
			if(Id==1):
				Id="Suresh Vairamuthu"
			elif(Id==2):
				Id="Vivek Lakshmanan"
		else:
			Id="Unknown"
		cv2.putText(im, Id, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
	cv2.imshow('im',im) 
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cam.release()
cv2.destroyAllWindows()