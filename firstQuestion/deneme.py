import matplotlib.pylab as plt
from PIL import Image
from numpy import pi, exp, sqrt
import numpy as np

s, k = 1, 2 #  generate a (2k+1)x(2k+1) gaussian kernel with mean=0 and sigma = s
probs = [exp(-z*z/(2*s*s))/sqrt(2*pi*s*s) for z in range(-k,k+1)]
kernel = np.outer(probs, probs)

img = Image.open('firstQuestion/image0.png').convert('L')
#Image._show(img)
value=list(img.getdata())
print(value)

s, k = 1, 2 #  generate a (2k+1)x(2k+1) gaussian kernel with mean=0 and sigma = s
probs = [exp(-z*z/(2*s*s))/sqrt(2*pi*s*s) for z in range(-k,k+1)]
kernel = np.outer(probs, probs)

a = np.array(kernel)
a.transpose()
print(a)

pix = img.load() # Get the width and hight of the image for iterating over

width, height = img.size
sum=0
array = (np.random.rand(height, width) * 256).astype(np.uint8)
for i in range (height): #traverses through height of the image
    for j in range (width): #traverses through width of the image
        try:
            sum+=kernel[0][0]*pix[j - 2 , i - 2]
        except:
            sum+=0
        try:
            sum+=kernel[1][0]*pix[j - 2 , i - 1]
        except:
            sum+=0
        try:
            sum+=kernel[2][0]*pix[j - 2 , i]
        except:
            sum+=0
        try:
            sum+=kernel[3][0]*pix[j - 2 , i + 1]
        except:
            sum+=0
        try:
            sum+=kernel[4][0]*pix[j - 2 , i + 2]
        except:
            sum+=0
        try:
            sum+=kernel[0][1]*pix[j - 1 , i - 2]
        except:
            sum+=0
        try:
            sum+=kernel[1][1]*pix[j - 1 , i - 1]
        except:
            sum+=0
        try:
            sum+=kernel[2][1]*pix[j - 1 , i]
        except:
            sum+=0
        try:
            sum+=kernel[3][1]*pix[j - 1 , i + 1]
        except:
            sum+=0
        try:
            sum+=kernel[4][1]*pix[j - 1 , i + 2]
        except:
            sum+=0
        try:
            sum+=kernel[0][2]*pix[j , i - 2]
        except:
            sum+=0
        try:
            sum+=kernel[1][2]*pix[j , i - 1]
        except:
            sum+=0
        try:
            sum+=kernel[2][2]*pix[j , i]
        except:
            sum+=0
        try:
            sum+=kernel[3][2]* pix[j , i + 1]
        except:
            sum+=0
        try:
            sum+=kernel[4][2]*pix[j , i + 2]
        except:
            sum+=0
        try:
            sum+=kernel[0][3]*pix[j + 1 , i - 2]
        except:
            sum+=0
        try:
            sum+=kernel[1][3]* pix[j + 1 , i - 1]
        except:
            sum+=0
        try:
            sum+=kernel[2][3]*pix[j + 1 , i]
        except:
            sum+=0
        try:
            sum+=kernel[3][3]*pix[j + 1 , i + 1]
        except:
            sum+=0
        try:
            sum+=kernel[4][3]*pix[j + 1 , i + 2]
        except:
            sum+=0
        try:
            sum+=kernel[0][4]*pix[j + 2 , i - 2]
        except:
            sum+=0
        try:
            sum+=kernel[1][4]*pix[j + 2 , i - 1]
        except:
            sum+=0
        try:
            sum+=kernel[2][4]*pix[j + 2 , i]
        except:
            sum+=0
        try:
            sum+=kernel[3][4]*pix[j + 2 , i + 1]
        except:
            sum+=0
        try:
            sum+=kernel[4][4]*pix[j + 2 , i + 2]
        except:
            sum+=0
        pix[j,i]=int(sum)
        #print(sum)
        sum=0






img = Image.fromarray(pix)
img.save('test.png')




