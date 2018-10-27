import numpy as np
import cv2


def main():

	cap = cv2.VideoCapture(0)

	while True:
		ret,frame = cap.read()

		# gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

		face_cascade =   cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')
		profile_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_profileface.xml')

		faces = face_cascade.detectMultiScale(frame,1.3,5)
		# faces_alt = face_alt_cascade.detectMultiScale(gray,1.3,5)
		profiles = profile_cascade.detectMultiScale(frame,1.3,5)

		print(len(faces))

		for (x,y,w,h) in faces:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)


		for (x,y,w,h) in profiles:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
			#cv2.imwrite('file.png',faces[0])

		cv2.imshow('live',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break;

	# cv2.destroyAllWindows()


if __name__ == '__main__':
	main()

