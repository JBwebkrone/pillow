"""Crop image """
from PIL import Image

# region is defined by a 4-tuple, where coordinates are (left, upper, right, lower)
box = (110, 110, 420,420)

def crop_image(box):
    """Cropping given image according to the given dimentions

    Args:
        left ([int]): [crop from left side]
        top ([int]): [crop from top side]
        right ([int]): [crop from right side]
        bottom ([int]): [crop from bottom side]
    """
    with Image.open('images/cats.jpg') as im:
        print(im.size)
        region = im.crop(box)
        region.transpose(Image.ROTATE_180) # Returns a 180 degree rotated copy of this image
        region.save("cropped.jpg")

