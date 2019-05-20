import cv2
from numpy import exp, sqrt
import numpy as np

face1 = cv2.imread('d1.png',0)
face2 = cv2.imread('d2.png',0)
face3 = cv2.imread('d3.png',0)

rows1, cols1 = face1.shape
rows2, cols2 = face2.shape
rows3, cols3 = face3.shape

cols=min(cols1,cols2,cols3)
rows=min(rows1,rows2,rows3)
avarage_face = np.zeros((rows, cols, 1), np.uint8)


for i in range(cols):
    for j in range(rows):
        sumOfFace=face1[j, i]+face2[j,i]+face3[j,i]
        avarageOfFace=sumOfFace/3
        avarage_face[j,i]=avarageOfFace

cv2.imshow("Blank Image", avarage_face)
cv2.imwrite('ümraniyeTayfa.jpg', avarage_face)
cv2.waitKey(0)
cv2.destroyAllWindows()