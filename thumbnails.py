"""Creating thumbnails """
import os, sys
from PIL import Image

def create_thumbnail(image_path="tree.jpg", width=128, height=128):
    try: 
        with Image.open(image_path) as im:
            im.thumbnail(size=(width, height)) # it will keep aspect ratio
            #im.resize((width, height)) # it just follow the parameters and might distrub image
            im.save(image_path, "JPEG")
    except OSError:
        print("cannot create thumbnail for ", image_path)


create_thumbnail()