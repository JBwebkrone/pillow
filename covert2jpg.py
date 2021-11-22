"""Reading and writing the Images """

import os, sys
from PIL import Image


for files in sys.argv[1:]:
    file, ext = os.path.splitext(files)
    print(file)
    outfile = file + ".jpg"
    if files != outfile:
        try:
            with Image.open(files) as im:
                im.save(outfile)
        except OSError:
            print("cannot convert", files)

# python3 convert2jpg.py <full/file/path/name.extention>