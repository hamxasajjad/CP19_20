import cv2
import numpy as np
import dlib
import sys
    
cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()

while True:
	ret,frame=cap.read()
	frame = cv2.flip(frame,1)
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces=detector(gray)
	for face in faces:
		x,y=face.left(),face.top()
		w,h=face.right(),face.bottom()
		
		cv2.rectangle(frame,(x,y),(w,h),(0,225,0),3)
	#cv2.imshow("gray",gray)
	cv2.imshow("frame",frame)
	
	if cv2.waitKey(1) == ord("s"):
		break
		
cap.release()
cv2.destroyAllWindows()
