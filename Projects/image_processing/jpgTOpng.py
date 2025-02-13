# Create  jpg to png convert file
# pass target folder name as argument
# add new folder anem as argument


import sys
import os
from PIL import Image, ImageFilter


# grab frist and second argument

image_folder = sys.argv[1]
output_folder = sys.argv[2]
print(image_folder, output_folder)

# check is new  / exits , if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
#outputolder = output_folder

# loop through original image list
# Convert all images
# save all image in the new folder

for fileName in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{fileName}')
    cleanName = os.path.splitext(fileName)[0]
    img.save(f'{output_folder}{cleanName}.png', 'png')
    print('All done!')

