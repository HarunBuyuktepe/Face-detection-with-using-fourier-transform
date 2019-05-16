"""
@file laplace_demo.py
@brief Sample code showing how to detect edges using the Laplace operator
"""
import sys
import cv2 as cv
import numpy
import np

from matplotlib import pyplot as plt
from scipy import ndimage
def laplacian(src,imageName):
    # [load]
    # [reduce_noise]
    # Remove noise by blurring with a Gaussian filter
    src = cv.GaussianBlur(src, (3, 3), 0)
    # [reduce_noise]
    # [convert_to_gray]
    # Convert the image to grayscale
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    # [convert_to_gray]
    # Create Window
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
    # [laplacian]
    # Apply Laplace function
    dst = cv.Laplacian(src_gray, ddepth, kernel_size)
    # [laplacian]
    # [convert]
    # converting back to uint8
    abs_dst = cv.convertScaleAbs(dst)
    # [convert]
    # [display]
    cv.imshow(window_name, abs_dst)
    cv.imwrite(imageName+"_output_laplacian.jpg", img=abs_dst)
    cv.waitKey(0)
    cv.destroyAllWindows()  # destroys the window showing image

    # [display]
def gaussian(src,imageName):
    # apply guassian blur on src image
    dst = cv.GaussianBlur(src, (5, 5), cv.BORDER_DEFAULT)

    # display input and output image
    cv.imshow("Gaussian Smoothing", numpy.hstack((src, dst)))
    cv.imwrite(imageName+"_output_gaussian_smothing.jpg",img=dst)
    cv.waitKey(0)  # waits until a key is pressed
    cv.destroyAllWindows()  # destroys the window showing image
def sobel(src,imageName):
    print("yapılacak")



# [variables]
# Declare the variables we are going to use
ddepth = cv.CV_16S
kernel_size = 3
window_name = "Laplace Filter"
# [variables]


def main(argv):


    #for i in range(4):
    imageName = 'image0.png'
    src = cv.imread(cv.samples.findFile(imageName), cv.IMREAD_COLOR)  # Load an image
    # Check if image is loaded fine
    if src is None:
        print('Error opening image')
        return -1
    print("ne")
    laplacian(src, imageName)
    gaussian(src, imageName)
    sobel(src,imageName)

    img = cv.imread('input.jpg')
#    cv.imshow('Original', img)

    size = 15

    # generating the kernel
    kernel_motion_blur = np.zeros((size, size))
    kernel_motion_blur[int((size - 1) / 2), :] = np.ones(size)
    kernel_motion_blur = kernel_motion_blur / size

    # applying the kernel to the input image
    output = cv.filter2D(img, -1, kernel_motion_blur)

    cv.imshow('Motion Blur', output)
    cv.waitKey(0)


    return 0
if __name__ == "__main__":
    main(sys.argv[1:])


