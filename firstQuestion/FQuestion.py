import cv2
import matplotlib.pylab as plt
import pic as pic
import scipy
import numpy as np
from PIL import Image
from numpy import pi, exp, sqrt
from scipy import ndimage, misc


def filter(imgname, kernel, name):
    pix = cv2.imread(imgname,0)
    height, width = pix.shape  # Get the width and height of the image for iterating over

    kernel_length = len(kernel)
    half_length = -int(kernel_length / 2)

    print(half_length)
    for i in range(height):  # traverses through height of the image
        for j in range(width):  # traverses through width of the image
            sum = 0
            tempx = i + half_length
            for kernelx in range(0, kernel_length):
                tempy = j + half_length
                for kernely in range(0, kernel_length):
                    if ((tempx + kernelx >= 0) & (tempy + kernely >= 0) & (tempy + kernely < width) & (tempx + kernelx < height)):
                        sum += kernel[kernelx][kernely] * pix[tempx+kernelx][tempy+kernely]
            pix[i,j] = sum
    img = Image.fromarray(pix, 'P')
    img.save(name + '.png')


def filter2(imgname, kernel, name):
    pix = cv2.imread(imgname, 0)
    height, width = pix.shape  # Get the width and height of the image for iterating over

    kernel_length = len(kernel)
    half_length = -int(kernel_length / 2)

    for i in range(height):  # traverses through height of the image
        for j in range(width):  # traverses through width of the image
            sum = 0
            tempx = i + half_length
            for kernelx in range(kernel_length):
                tempy = j + half_length
                for kernely in range(kernel_length):
                    try:
                        sum += kernel[kernelx][kernely] * pix[tempx + kernelx][tempy + kernely]
                    except:
                        sum += kernel[kernelx][kernely] * pix[tempx][tempy]
            pix[i][j] = int(sum)
    img = Image.fromarray(pix, 'P')
    img.save(name + '.png')


array3 = np.zeros((3, 3))
array3[1, 1] = 1

array5 = np.zeros((5, 5))
array5[2, 2] = 1

laplacian = np.array((
   [0.1, 0.1, 0.1],
   [0.1, -1, 0.1],
   [0.1, 0.1, 0.1]), dtype="int")
# scipy.ndimage.laplace(array3)
print(laplacian)

sobel = scipy.ndimage.sobel(array3)
print(sobel)

gaussian = scipy.ndimage.gaussian_filter(array5, 5)
print(gaussian)

motion = [[0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.010661, 0.004530,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.013200, 0.045068, 0.010661,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.013200, 0.045068, 0.013200, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.013200, 0.045068, 0.013200, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.013200, 0.045068, 0.013200, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.013200, 0.045068, 0.013200, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.013200, 0.045068, 0.013200, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.013200, 0.045068, 0.013200, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.013200, 0.045068, 0.013200, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.013200, 0.045068, 0.013200, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.013200,
           0.045068, 0.013200, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.013200, 0.045068,
           0.013200, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.013200, 0.045068, 0.013200,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.013200, 0.045068, 0.013200, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.045068, 0.013200, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
           0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000]]

filter('cameraman.tif', gaussian, "c-gaussian")
filter('cameraman.tif', laplacian, "c-laplacian")
filter('cameraman.tif', sobel, "c-sobel")
#filter('cameraman.tif', motion, "c-motion")

filter2('cameraman.tif', gaussian, "c-gaussian2")
filter2('cameraman.tif', laplacian, "c-laplacian2")
filter2('cameraman.tif', sobel, "c-sobel2")
#filter2('cameraman.tif', motion, "c-motion2")
