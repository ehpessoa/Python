#!python3
# resize_and_add_logo.py - loops over cwd to find all jpg and png files, resize to 300x300 and add logo.

import os
from PIL import Image

# TODO extend to modify GIF, Pillow does not support gif, image is not animated

square_fit_size = 300
logo_filename = 'catlogo.png'

os.makedirs('with_logo', exist_ok=True)

# open logo image, get width and height
logo_image = Image.open(logo_filename)
logo_width, logo_height = logo_image.size

# iterate through files in current working directory
for filename in os.listdir('.'):
    # skip file if logo, or not .png, .jpg, .gif, .bmp
    if not ((filename.lower().endswith('.png') or filename.lower().endswith('.jpg') or filename.lower().endswith(
            '.gif') or filename.lower().endswith('.bmp'))) or (filename == logo_filename):
        continue
    # open file and get size
    else:
        current_image = Image.open(filename)
        width, height = current_image.size
        # check for 2x the size of the logo
        if width < 2 * logo_width or height < 2 * logo_height:
            continue
        # check if resizing is needed
        if width > square_fit_size and height > square_fit_size:
            if width > height:
                # get integer, not float
                height = int((square_fit_size / width) * height)
                width = square_fit_size
            else:
                # get integer, not float
                width = int((square_fit_size / height) * width)
                height = square_fit_size
            print(f'Resizing {filename}')
            current_image = current_image.resize((width, height))
        print(f'Adding logo to {filename}')
        current_image.paste(im=logo_image, box=(width - logo_width, height - logo_height), mask=logo_image)
        # save changes
        current_image.save(os.path.join('with_logo', filename))
