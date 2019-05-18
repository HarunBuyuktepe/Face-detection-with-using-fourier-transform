import cv2
from numpy import exp, sqrt
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
        avarage_face[j,i]=int(avarageOfFace)

cv2.imshow("Blank Image", avarage_face)
cv2.imwrite('avarage_face.jpg', avarage_face)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""M[x,y]=1/pq * toplam r sıfırdan p-1 e içinde toplam s sıfırdan q-1 I[x+r][y+s] """

image=cv2.imread('t3.png',0)
height, width = image.shape
m_matrix= np.zeros((height, width, 1), np.uint8)

for i in range(height):
    for j in range(width):
        sum = 0
        for k in range(height-i):
            for l in range(width-j):
              sum+=image[i+k,j+l]

        m_matrix[i,j]=int(sum/(height*width))
#print(m_matrix)

sum=0
for k in range(height ):
    for l in range(width ):
        sum += avarage_face[ k,l]
Mt=sum/(height*width)

#print(Mt)


a_matrix= np.zeros((height, width, 1), np.uint8)

for i in range(height):
    for j in range(width):
        up=0
        down1=0
        down2=0
        for k in range(height - i):
            for l in range(width - j):

                up+=(avarage_face[k,l]-Mt)*(image[i+k,j+l]-m_matrix[i,j])
                down1+=((avarage_face[k, l] - Mt)*(avarage_face[k, l] - Mt))
                down2+=((image[i+k,j+l]-m_matrix[i,j])*(image[i+k,j+l]-m_matrix[i,j]))

        sum=up/(sqrt(down2)*sqrt(down1))
        a_matrix[i,j]=sum
print(a_matrix)

# Find index of maximum value from 2D numpy array
result = np.where(a_matrix == np.amax(a_matrix))

print('Tuple of arrays returned : ', result)

print('List of coordinates of maximum value in Numpy array : ')
# zip the 2 arrays to get the exact coordinates
listOfCordinates = list(zip(result[0], result[1]))
# travese over the list of cordinates
for cord in listOfCordinates:
    print(cord)


















