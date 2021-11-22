"""Dealing with multiple files in dir(s) """

from PIL import Image
import glob

path = "images/pen/*"

for img in glob.glob(path):
    print(img)
    with Image.open(img) as im:
        gray = im.convert("L") # default method of converting a greyscale ("L")
        rotated45 = gray.rotate(45, expand=True)
        rotated45.save(img.split(".")[0] + "_rotated.jpeg", "JPEG")