from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2


def rect_to_bb(rect):
	x = rect.left()
	y = rect.top()
	w = rect.right() - x
	h = rect.bottom() - y
	return (x, y, w, h)
    

def shape_to_np(shape, dtype="int"):
	coords = np.zeros((68, 2), dtype=dtype)
	for i in range(0, 68):
		coords[i] = (shape.part(i).x, shape.part(i).y)
	return coords
    
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"C:\Users\Nitin_Tyagi\Downloads\Nitin\practice\face_detection\shape_predictor_68_face_landmarks.dat")

image = cv2.imread(r'C:\Users\Nitin_Tyagi\Downloads\Nitin\practice\face_detection\input_images\Nitin3.jpg')
image = imutils.resize(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rects = detector(gray, 1)

for (i, rect) in enumerate(rects):
	shape = predictor(gray, rect)
	shape = face_utils.shape_to_np(shape)
	(x, y, w, h) = face_utils.rect_to_bb(rect)
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
	cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
	#for (x, y) in shape:
	#	cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
cv2.imwrite(r'C:\Users\Nitin_Tyagi\Downloads\Nitin\practice\face_detection\output\output3.jpg', image)
cv2.imshow("Output", image)
cv2.waitKey(0)