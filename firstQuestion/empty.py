import numpy
from PIL import Image

img = Image.open('image0.png').convert('L')
imgarr = numpy.array(img)

print(imgarr[40][40])
print(imgarr.shape)

