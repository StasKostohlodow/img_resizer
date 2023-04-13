from PIL import Image
import os

open_folder = 'img'
saver_folder = 'resize-img'
open_path = f"{os.path.dirname(__file__)}\\{open_folder}\\"
saver_path = f"{os.path.dirname(__file__)}\\{saver_folder}\\"

if not os.path.exists(saver_folder):
    os.makedirs(saver_folder)

files = os.listdir(open_path)

width = int(input("Enter width (0 for auto): "))
height = int(input("Enter height (0 for auto): "))

for file in files:
    image = Image.open(open_path+file)

    new_width = width
    new_height = height
    if width==0:
        new_width = int(height*image.size[0]/image.size[1])
    elif height==0:
        new_height = int(width*image.size[1]/image.size[0])
        

    resized_image = image.resize((new_width, new_height))
    resized_image.save(saver_path+file)


