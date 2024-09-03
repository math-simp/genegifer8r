## Copyright CCB
import imageio.v2 as imageio
from PIL import Image

# Change this as you please
gifname = "nos-pp.gif"
filenames = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg"]
target_size = (500, 500)


def openjpg(filename):
    return Image.open(filename)


def convert(img):
    return img.convert("RGB")


def reshape(img):
    return img.resize(target_size)


def rotate(img):
    return img.rotate(0)


# List Comprehension
images = [rotate(reshape(convert(openjpg(filename)))) for filename in filenames]

imageio.mimsave(gifname, images, fps=2, loop=0)
