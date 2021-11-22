"""Combine 2 images or overlap images """
from PIL import Image

def combine(back_image, front_image):
    """Combining the two images with custom size of 'front_image'

    Args:
        back_image (image): the image which will be on background
        front_image (image): foremost or front image
    """
    try:
        img1 = Image.open(back_image)
        img2 = Image.open(front_image)

        img1_copy = img1.copy()
        #img1_copy.paste(img2, (320, 320)) # Pastes img2 image into img1_copy image.
        img1_copy.paste(img2)
        img1_copy.save("combined_image.jpg")

        img1.close()
        img2.close()
    except:
        print("Unable to combine")

combine("images/cats.jpg", "images/ruler.png")