from PIL import Image
import os

open_folder = 'img'
saver_folder = 'resize-img'



files = os.listdir(open_folder)

width = int(input("Enter width (0 for auto): "))
height = int(input("Enter height (0 for auto): "))

if not os.path.exists(saver_folder):
    os.makedirs(saver_folder)
    
for file in files:
    image = Image.open(open_folder+'\\'+file)
    new_width = width
    new_height = height
    if width==0:
        new_width = int(height*image.size[0]/image.size[1])
    elif height==0:
        new_height = int(width*image.size[1]/image.size[0])
    resized_image = image.resize((new_width, new_height))
    resized_image.save(saver_folder+'\\'+file)

input("Enter any to close programm")

