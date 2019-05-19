import cv2
from numpy import exp, sqrt
import numpy as np

face1 = cv2.imread('t2face.jpg',0)
face2 = cv2.imread('t2face.jpg',0)
face3 = cv2.imread('t2face.jpg',0)


rows, cols = face3.shape

avarage_face = np.zeros((rows, cols, 1), np.uint8)


for i in range(cols):
    for j in range(rows):
        sumOfFace=face1[j, i]+face2[j,i]+face3[j,i]
        avarageOfFace=sumOfFace/3
        avarage_face[j,i]=int(avarageOfFace)

cv2.imshow("Blank Image", avarage_face)
cv2.imwrite('avarage_face.jpg', avarage_face)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""M[x,y]=1/pq * toplam r sıfırdan p-1 e içinde toplam s sıfırdan q-1 I[x+r][y+s] """

image=cv2.imread('t2.jpg',0)
height, width = image.shape
m_matrix= np.zeros((height, width, 1), np.uint8)

#şurdan aşağısını kontrol eder misin

sum=0
for k in range(rows):
    for l in range(cols):
        sum += avarage_face[k,l]
Mt=sum/(cols*rows)

print(Mt)


a_matrix= np.zeros((height, width, 1), np.uint8)
print(height-rows)
for i in range(height-rows):
    for j in range(width-cols):
        sum = 0
        m_i=0
        for k in range(rows):
            for l in range(cols):
                sum += (image[i + k, j + l])

        m_i = (sum / (rows * cols))

        up=0
        down1=0
        down2=0
        for k in range(rows):
            for l in range(cols):
                up += (avarage_face[k, l] - Mt) * (image[i + k, j + l] - m_i)
                down1 += ((avarage_face[k, l] - Mt) * (avarage_face[k, l] - Mt))
                down2 += ((image[i + k, j + l] - m_i) * (image[i + k, j + l] - m_i))
        left=sqrt(down1)
        right=sqrt(down2)
        x  = up/(left*right)
        a_matrix[i,j]=x
        print(x,'niye girmedi',i,'soldaki x sağdaki y',j)

result = np.where(a_matrix == np.amax(a_matrix))

print('Returned tuple of arrays :', result)
print('List of Indices of maximum element :', result[0])

cv2.rectangle(image,(3,17),(3+cols,17+rows),(0,255,0),1)
cv2.imwrite('new.png',image)





















