"""Image processing library """
from PIL import Image

im_jpg = Image.open('images/cats.jpg') # load an image from a file
im_webp = Image.open('images/insects.webp') # load an image from a file
im_gif = Image.open('images/prism.gif') # load an image from a file
im_png = Image.open('images/values.png') # load an image from a file

print("----------------------------------------------------")
print(im_jpg.format, im_jpg.size, im_jpg.mode) # JPEG (1280, 852) RGB
print(im_webp.format, im_webp.size, im_webp.mode) # WEBP (6370, 3453) RGB
print(im_gif.format, im_gif.size, im_gif.mode) # GIF (700, 435) P
print(im_png.format, im_png.size, im_png.mode) # PNG (1020, 1024) P
print("----------------------------------------------------")


rotate45 = im_jpg.rotate(45) # without edges
rotate45.save("rotated45.jpg")

rotate45expand = im_jpg.rotate(45, expand=True) # with edges
rotate45expand.save("rotated45expand.jpg")



im_jpg.close()
im_webp.close()
im_gif.close()
im_png.close()