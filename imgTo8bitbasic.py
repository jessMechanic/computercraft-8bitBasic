
# Importing Image from PIL package
from PIL import Image
import sys
import os
redo = True
while redo:
      print("please type/past the path of the img")
      path = input()
      path = path.replace('"',"")
      print(path)
      isFile = os.path.isfile(path)
      if(isFile == False):
           print("this is not a path")
      
      else:
            redo = False
      
doBreak = False
im = Image.open(path)
im = im.convert("RGBA")
width, height = im.size
print(width)
print(height)
imageData = ""
for  y in  range(height):
    for  x in range(width):
      if(doBreak):
            break
      coordinate = x, y = x, y
      if(im.getpixel(coordinate) == (240, 240, 240, 255)):
        imageData += "0"
      elif (im.getpixel(coordinate) == (242, 178, 51, 255)):
            imageData += "1"
      elif (im.getpixel(coordinate) == (229, 127, 216, 255)):
            imageData += "2"
      elif (im.getpixel(coordinate) == (153, 178, 242, 255)):
            imageData += "3"
      elif (im.getpixel(coordinate) == (222, 222, 108, 255)):
            imageData += "4"
      elif (im.getpixel(coordinate) == (127, 204, 25, 255)):
            imageData += "5"
      elif (im.getpixel(coordinate) == (242, 178, 204, 255)):
            imageData += "6"
      elif (im.getpixel(coordinate) == (76, 76, 76, 255)):
            imageData += "7"
      elif (im.getpixel(coordinate) == (153, 153, 153, 255)):
            imageData += "8"
      elif (im.getpixel(coordinate) == (76, 153, 178, 255)):
            imageData += "9"
      elif (im.getpixel(coordinate) == (178, 102, 229, 255)):
            imageData += "a"
      elif (im.getpixel(coordinate) == (51, 102, 204, 255)):
            imageData += "b"
      elif (im.getpixel(coordinate) == (127, 102, 76, 255)):
            imageData += "c"
      elif (im.getpixel(coordinate) == (87, 166, 78, 255)):
            imageData += "d"
      elif (im.getpixel(coordinate) == (204, 76, 76, 255)):
            imageData += "e"
      elif (im.getpixel(coordinate) == (25, 25, 25, 255)):
            imageData += "f"
      else:
            print("a not supported color found")
            doBreak = True
            break




            
print(imageData)

input()