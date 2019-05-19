import matplotlib.pylab as plt
import pic as pic
import scipy
import numpy as np
from PIL import Image
from numpy import pi, exp, sqrt
from scipy import ndimage, misc


def filter(img, kernel, name):
    pix = np.array(img)
    width, height = img.size  # Get the width and height of the image for iterating over
    sum = 0
    lent = len(kernel)
    lentt = -int(lent/2)
    temp1 = lentt
    temp2 = lentt
    print(lentt)
    for i in range(height):  # traverses through height of the image
        for j in range(width):  # traverses through width of the image
            for kk in range(lent):
                for l in range(lent):
                    try:
                        sum += kernel[kk][l] * pix[i + temp1][j + temp2]
                    except:
                        sum += 0
                    temp2 += 1
                temp1 += 1
                temp2 = lentt
            temp1 = lentt
            pix[i][j] = sum
            sum = 0

    img = Image.fromarray(pix, 'P')
    img.save(name + '.png')


img = Image.open('lena.bmp').convert('L')

array3 = np.zeros((3, 3))
array3[1, 1] = 1

array5 = np.zeros((5, 5))
array5[2, 2] = 1

laplacian = scipy.ndimage.laplace(array3)
print(laplacian)

sobel = scipy.ndimage.sobel(array3)
print(sobel)

gaussian2 = scipy.ndimage.gaussian_filter(array5,5)
#print(gaussian2)

filter(img, gaussian2, "hzgaussian")
filter(img, laplacian, "hzlaplacian")
filter(img, sobel, "hzsobel")
