import cv2

import numpy as np


face1 = cv2.imread('t1.png', 0)
face2=cv2.imread('t2.png',0)
face3=cv2.imread('t3.png',0)

rows, cols = face3.shape

avarage_face = np.zeros((rows, cols, 1), np.uint8)


for i in range(cols):
    for j in range(rows):
        sumOfFace=face1[j, i]+face2[j,i]+face3[j,i]
        avarageOfFace=sumOfFace/3
        image[j,i]=int(avarageOfFace)

cv2.imshow("Blank Image", avarage_face)
cv2.imwrite('avarage_face.jpg', avarage_face)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""M[x,y]=1/pq * toplam r sıfırdan p-1 e içinde toplam s sıfırdan q-1 I[x+r][y+s] """



