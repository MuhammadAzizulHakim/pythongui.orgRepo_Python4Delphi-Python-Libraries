from __future__ import print_function
from PIL import Image
import os
 
path = "C:/Users/YOUR_USERNAME/cat1.jpg"
im = Image.open(path)
size = (250, 250)
outfile = os.path.splitext(path)[0] + "Resized.jpg"
 
im.thumbnail(size)
im.save(outfile, "JPEG")