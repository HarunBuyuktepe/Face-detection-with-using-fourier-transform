import matplotlib.pylab as plt
import numpy as np
from PIL import Image
from numpy import pi, exp, sqrt
# use a (r, g, b) tuple to represent colors
red = (255,0,0)
white = (3,3,3)

# create a new 256x256 pixel image surface
# make the background white (default bg=black)
im = Image.open('image0.png', 'r')
rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((1, 1))
print(r, g, b)
width, height = im.size
#Image._show(im)
# keep y fixed to create a horizontal line
y = 10
for x in range(1,width ):
    # put a red pixel at point (x, y)
    im.putpixel((x, y), red)
# save the image
im.save("test1.png")
# optionally look at the image you have created
#im.show()


s, k = 1, 2 #  generate a (2k+1)x(2k+1) gaussian kernel with mean=0 and sigma = s
probs = [exp(-z*z/(2*s*s))/sqrt(2*pi*s*s) for z in range(-k,k+1)]
kernel = np.outer(probs, probs)

print(kernel[2][2])
#[[ 0.00291502  0.00792386  0.02153928  0.00792386  0.00291502]
#[ 0.00792386  0.02153928  0.05854983  0.02153928  0.00792386]
#[ 0.02153928  0.05854983  0.15915494  0.05854983  0.02153928]
#[ 0.00792386  0.02153928  0.05854983  0.02153928  0.00792386]
#[ 0.00291502  0.00792386  0.02153928  0.00792386  0.00291502]]

#plt.imshow(kernel)
#plt.colorbar()
#plt.show()

width, height = im.size

i=1
j=1
for i in range(1,width):
    #print("i=",i)
    r, g, b = rgb_im.getpixel((i, j))
    r = r * kernel[2][2]
    g = g * kernel[2][2]
    b = b * kernel[2][2]
    #print(r, g, b)
    im.putpixel((x, y), white)
    for j in range(1,height):
        r, g, b = rgb_im.getpixel((i, j))
        r = r * kernel[2][2]
        g = g * kernel[2][2]
        b = b * kernel[2][2]
        #print(r, g, b)
        im.putpixel((x, y), (int(r),int(g),int(b)))
im.show()
print(kernel[2])


