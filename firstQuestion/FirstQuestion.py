import cv2
import matplotlib.pylab as plt
import pic as pic
import scipy
import numpy as np
from PIL import Image
from numpy import pi, exp, sqrt
from scipy import ndimage, misc


def filter(imgname, kernel, name):
    image = cv2.imread(imgname,0)
    height, width = image.shape

    if len(kernel[0]) == 5:#gaussian
        for i in range(height):
            for j in range(width):
                value = 0
                tempx = i + 2
                for kernelX in range(0, 5):
                    tempy = j + 2
                    for kernelY in range(0, 5):
                        if ((tempx + kernelX >= 0) & (tempy + kernelY >= 0) & (tempy + kernelY < width) & (
                                tempx + kernelX < height)):
                            value += image[tempx + kernelX][tempy + kernelY] * kernel[kernelX][kernelY]
                image[i,j]=value


    if len(kernel[0]) == 3:#gaussian
        for i in range(height):
            for j in range(width):
                value = 0
                tempx = i - 1
                tempy = j - 1

                for kernelX in range(0, 3):
                    for kernelY in range(0, 3):
                        if ((tempx + kernelX >= 0) & (tempy + kernelY >= 0) & (tempy + kernelY < width) & (tempx + kernelX < height)):
                            value += image[tempx + kernelX][tempy + kernelY] * kernel[kernelX][kernelY]
                image[i,j]=value
    img = Image.fromarray(image, 'P')
    img.save(name + '.png')


array5 = np.zeros((5, 5))
array5[2, 2] = 1

array3 = np.zeros((3, 3))
array3[1, 1] = 1

gaussian_kernel = scipy.ndimage.gaussian_filter(array5, 5)
print(gaussian_kernel)

laplacian_kernel = np.array((
   [0.1,0.1 ,0.1],
   [0.1, -1,0.1],
   [0.1, 0.1,0.1]), dtype="int")



sobel_kernel = scipy.ndimage.sobel(array3)

filter('cameraman.tif',laplacian_kernel,'Laplacian')
filter('cameraman.tif',gaussian_kernel,'Gaussian')
filter('cameraman.tif',sobel_kernel,'Sobel')
