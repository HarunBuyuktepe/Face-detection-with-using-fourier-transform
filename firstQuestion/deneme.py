import matplotlib.pylab as plt
import pic as pic
from PIL import Image
from numpy import pi, exp, sqrt
import numpy as np


def filter(img,kernel,name):
    pix = np.array(img)
    width, height = img.size  # Get the width and hight of the image for iterating over
    print(width, height)
    sum = 0
    for i in range(height):  # traverses through height of the image
        for j in range(width):  # traverses through width of the image
            try:
                sum += kernel[0][0] * pix[i - 2][j - 2]
            except:
                sum += 0
            try:
                sum += kernel[1][0] * pix[i - 2][j - 1]
            except:
                sum += 0
            try:
                sum += kernel[2][0] * pix[i - 2][j]
            except:
                sum += 0
            try:
                sum += kernel[3][0] * pix[i - 2][j + 1]
            except:
                sum += 0
            try:
                sum += kernel[4][0] * pix[i - 2][j + 2]
            except:
                sum += 0
            try:
                sum += kernel[0][1] * pix[i - 1][j - 2]
            except:
                sum += 0
            try:
                sum += kernel[1][1] * pix[i - 1][j - 1]
            except:
                sum += 0
            try:
                sum += kernel[2][1] * pix[i - 1][j]
            except:
                sum += 0
            try:
                sum += kernel[3][1] * pix[i - 1][j + 1]
            except:
                sum += 0
            try:
                sum += kernel[4][1] * pix[i - 1][j + 2]
            except:
                sum += 0
            try:
                sum += kernel[0][2] * pix[i][j - 2]
            except:
                sum += 0
            try:
                sum += kernel[1][2] * pix[i][j - 1]
            except:
                sum += 0
            try:
                sum += kernel[2][2] * pix[i][j]
            except:
                sum += 0
            try:
                sum += kernel[3][2] * pix[i][j + 1]
            except:
                sum += 0
            try:
                sum += kernel[4][2] * pix[i][j + 2]
            except:
                sum += 0
            try:
                sum += kernel[0][3] * pix[i + 1][j - 2]
            except:
                sum += 0
            try:
                sum += kernel[1][3] * pix[i + 1][j - 1]
            except:
                sum += 0
            try:
                sum += kernel[2][3] * pix[i + 1][j]
            except:
                sum += 0
            try:
                sum += kernel[3][3] * pix[i + 1][j + 1]
            except:
                sum += 0
            try:
                sum += kernel[4][3] * pix[i + 1][j + 2]
            except:
                sum += 0
            try:
                sum += kernel[0][4] * pix[i + 2][j - 2]
            except:
                sum += 0
            try:
                sum += kernel[1][4] * pix[i + 2][j - 1]
            except:
                sum += 0
            try:
                sum += kernel[2][4] * pix[i + 2][j]
            except:
                sum += 0
            try:
                sum += kernel[3][4] * pix[i + 2][j + 1]
            except:
                sum += 0
            try:
                sum += kernel[4][4] * pix[i + 2][j + 2]
            except:
                sum += 0

            pix[i][j] = int(sum)
            # print(sum)
            sum = 0

    img = Image.fromarray(pix, 'P')
    img.save(name+'.png')

img = Image.open('image0.png').convert('L')

#gaussian kerneli yani filtresi
s, k = 1, 2 #  generate a (2k+1)x(2k+1) gaussian kernel with mean=0 and sigma = s
probs = [exp(-z*z/(2*s*s))/sqrt(2*pi*s*s) for z in range(-k,k+1)]
kernel = np.outer(probs, probs)

gaussian = np.array(kernel)
gaussian.transpose()
print(gaussian)


filter(img,gaussian,"gaussian")




