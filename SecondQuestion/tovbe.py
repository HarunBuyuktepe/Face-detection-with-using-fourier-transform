import cv2
import math
from numpy import exp, sqrt
import numpy as np


image=cv2.imread('bbb.jpg',0)
height, width = image.shape
m_matrix= np.zeros((height, width, 1), np.uint8)

face1 = cv2.imread('bbb1.jpg',0)
face2 = cv2.imread('bbb1.jpg',0)
face3 = cv2.imread('bbb1.jpg',0)


rows1, cols1 = face1.shape
rows2, cols2 = face2.shape
rows3, cols3 = face3.shape

cols=min(cols1,cols2,cols3)
rows=min(rows1,rows2,rows3)
avarage_face = np.zeros((rows, cols, 1), np.uint8)


for k in range(rows):
    for m in range(cols):
        avarage_face[k][m]=face1[k][m]+face2[k][m]+face3[k][m]
       # print(avarage_face[k][m])

rowsFace=rows
colsFace =cols
rows, cols = image.shape

sumOfTemplate = 0
meanOfTemplate = 0

correlationArray=[[0 for x in range(rows)],[0 for y in range(cols)]]

for i in range(rowsFace):
    for j in range(colsFace):
        sumOfTemplate+=avarage_face[i,j]

meanOfTemplate=sumOfTemplate/(rowsFace*colsFace)
print(meanOfTemplate)

for k in range(rows - rowsFace):
    for m in range(cols - colsFace):
        sumOfOrigin = 0
        correlation = 0
        meanOfOrigin = 0
        for i in range(rowsFace):
            for j in range(colsFace):
                if m + j < cols and k + i < rows:
                    sumOfOrigin += image[k + i, m + j]
        meanOfOrigin = sumOfOrigin / (rowsFace * colsFace)
        top = 0
        leftBottom = 0
        rightBottom = 0

        for q in range(rowsFace):
            for w in range(colsFace):
                top += ((avarage_face[q][w] - meanOfTemplate) * (image[q + k][w + m] - meanOfOrigin))
                leftBottom += ((avarage_face[q][w] - meanOfTemplate) * (avarage_face[q][w] - meanOfTemplate))
                rightBottom += ((image[q + k][w + m] - meanOfOrigin) * (image[q + k][w + m] - meanOfOrigin))
        correlationArray[k][m] = top / ((math.sqrt(leftBottom)) * (math.sqrt(rightBottom)))

for k in range(rows):
    for m in range(cols):
        print(correlationArray[k][m])


















