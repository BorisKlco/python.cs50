import sys
import os
from PIL import ImageOps
from PIL import Image


def arg():
    if len(sys.argv) < 3:
        return f"too few arg"
    if len(sys.argv) > 3:
        return f"too many"
    else:
        return isImg(sys.argv[1], sys.argv[2])


def isImg(imgRealOne, imgRealTwo):
    ext = [".jpg", ".jpeg", ".png"]
    imgOne = os.path.splitext(imgRealOne)
    imgTwo = os.path.splitext(imgRealTwo)
    if imgOne[1].lower() not in ext:
        return f"Inalid input"
    if imgTwo[1].lower() not in ext:
        return f"Invalid output"
    else:
        if imgOne[1].lower() == imgTwo[1].lower():
            return convert(imgRealOne, imgRealTwo)
        else:
            return f"Input and output have different extensions"


def convert(imgOne, imgTwo):
    try:
        photo = Image.open(imgOne)
        shirt = Image.open("shirt.png")
        edit = ImageOps.fit(photo, shirt.size)
        edit.paste(shirt, shirt)
        edit.save(imgTwo)
        return f""

    except:
        return f"File doesnt exist"


print(arg())
