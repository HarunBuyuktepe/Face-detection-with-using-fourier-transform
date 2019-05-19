import matplotlib.pylab as plt
import pic as pic
import scipy
from PIL import Image
from numpy import pi, exp, sqrt
import numpy as np
from scipy import ndimage, misc


def filter(img, kernel, name):
    pix = np.array(img)
    width, height = img.size  # Get the width and height of the image for iterating over
    print(width, height)
    sum = 0
    temp1 = -2
    temp2 = -2
    for i in range(height):  # traverses through height of the image
        for j in range(width):  # traverses through width of the image
            for kk in range(5):
                for l in range(5):
                    try:
                        sum += kernel[kk][l] * pix[i+temp1][j+temp2]
                    except:
                        sum += 0
                    temp2 += 1

                temp1 += 1
                temp2 = -2
            temp1 = -2
            pix[i][j] = int(sum)
            sum = 0

    img = Image.fromarray(pix, 'P')
    img.save(name + '.png')


img = Image.open('image0.png').convert('L')

# gaussian kerneli yani filtresi
s, k = 1, 2  # generate a (2k+1)x(2k+1) gaussian kernel with mean = 0 and sigma = s
probs = [exp(-z * z / (2 * s * s)) / sqrt(2 * pi * s * s) for z in range(-k, k + 1)]
kernel = np.outer(probs, probs)

gaussian = np.array(kernel)
gaussian.transpose()
#print(gaussian)

array5 = np.zeros((5, 5))
array5[2, 2] = 1

gaussian2 = scipy.ndimage.gaussian_filter(array5,5)
print(gaussian2)

filter(img, gaussian2, "gaussian")
