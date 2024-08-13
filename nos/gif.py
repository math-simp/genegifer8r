import imageio.v2 as imageio
from PIL import Image
import numpy as np
filenames = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg']
images = []

for filename in filenames:
    img = Image.open(filename)
    img = img.convert("RGB")
    img = img.rotate(270, expand=True)
    img_np = np.array(img)
    images.append(img_np)

imageio.mimsave('livi_v4.gif', images, fps=1, loop=0)
