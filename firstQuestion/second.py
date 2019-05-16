import numpy as np
import cv2
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def threshold_slow(T, image):
    # grab the image dimensions
    h = image.shape[0]
    w = image.shape[1]

    # loop over the image, pixel by pixel
    for y in range(0, h):
        for x in range(0, w):
            # threshold the pixel
            image[y, x] = 255 if image[y, x] >= T else 0

    # return the thresholded image
    return image

im = Image.open('image0.png', 'r')
#Image._show(im)
pix_val = list(im.getdata())
pix_val_flat = [x for sets in pix_val for x in sets]
print(pix_val)
print("Harun"
      "\n"
      "Harun")


image = threshold_slow(5, im)
plt.imshow(image, cmap="gray")

import cython

    @cython.boundscheck(False)
    def unsigned char[:, :] threshold_fast(int T, unsigned char [:, :] image):
    # set the variable extension types
    cdef int x, y, w, h

    # grab the image dimensions
    h = image.shape[0]
    w = image.shape[1]

     # loop over the image
     for y in range(0, h):
        for x in range(0, w):
            # threshold the pixel
            image[y, x] = 255 if image[y, x] >= T else 0

     # return the thresholded image
     return image