import cv2
import math

originImage=cv2.imread('t.jpg')
originImageFace =cv2.imread('ff.jpg')
image_grayscale =cv2.imread('t.jpg',0)
template_face_grayscale = cv2.imread('ff.jpg',0)

rowsFace, colsFace = template_face_grayscale.shape
rows, cols = image_grayscale.shape

sumOfTemplate = 0
meanOfTemplate = 0

correlationArray=[[0 for x in range(cols)] for y in range(rows)]

for i in range(rowsFace):
    for j in range(colsFace):
        sumOfTemplate+=template_face_grayscale[i,j]

meanOfTemplate=sumOfTemplate/(rowsFace*colsFace)


for i in range(rows-rowsFace):
    for j in range(cols-colsFace):
        sumOfOrigin=0
        meanOfOrigin=0
        for k in range(rowsFace):
            for e in range(colsFace):
                sumOfOrigin+=image_grayscale[i+k][j+e]
        meanOfOrigin=sumOfOrigin/(rowsFace*colsFace)
        top=0
        left=0
        right=0
        for x in range(rowsFace):
            for y in range(colsFace):
                top += ((template_face_grayscale[x][y] - meanOfTemplate) * (image_grayscale[i + x][y + j] - meanOfOrigin))
                left += ((template_face_grayscale[x][y]) - meanOfTemplate) * ((template_face_grayscale[x][y]) - meanOfTemplate)
                right += ((image_grayscale[i + x][y + j]) - meanOfOrigin) * ((image_grayscale[i + x][y + j]) - meanOfOrigin)
        left = math.sqrt(left)
        right = math.sqrt(right)
        print("i",i,"j",j)
        correlationArray[i][j] = abs(top / (left * right))

max=0
k=0
t=0
maxIndexX=0
maxIndexY=0
for i in correlationArray:
    t=0
    for j in i:
        if abs(j)>max:
            maxIndexX=k
            maxIndexY=t
            max=j
        t += 1
    k+=1

print(max)
print(k)
print(t)

print(correlationArray[maxIndexX][maxIndexY])
cv2.rectangle(image_grayscale,(maxIndexY,maxIndexX),(maxIndexY+colsFace,maxIndexX+rowsFace),(0,76,0),1)


cv2.rectangle(originImage,(maxIndexY,maxIndexX),(maxIndexY+colsFace,maxIndexX+rowsFace),(206, 120, 200),1)
cv2.line(originImage,(maxIndexY+int(colsFace/2),maxIndexX),(maxIndexY+int(colsFace/2),maxIndexX+rowsFace),(166, 120, 200),1)
cv2.line(originImage,(maxIndexY,maxIndexX+int(rowsFace/2)),(maxIndexY+colsFace,maxIndexX+int(rowsFace/2)),(166, 120, 200),1)
cv2.imwrite('gunah.png',originImage)

cv2.imshow('Final image', image_grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()