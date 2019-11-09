#! python3
# custom_seating_cards.py - Creates a custom seating card for guest list

import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('custom_seating_cards', exist_ok=True)

# open background
background = Image.open('flower.jpg')

# open guest list
with open('guests.txt', 'r') as guest_file:
    # get guest list and remove \n
    guest_list = [guest.replace('\n','') for guest in guest_file.readlines()]
    # for each guest on guest list, create new image
    for guest in guest_list:
        # open new image
        new_image = Image.new('RGBA', (360, 203), 'white')
        # paste background
        new_image.paste(im=background)
        # draw black rectangle
        draw = ImageDraw.Draw(new_image)
        draw.rectangle((0, 0, 360, 203), outline='black')
        # get font
        fonts_folder = 'C:\Windows\Fonts'
        arial_font = ImageFont.truetype(os.path.join(fonts_folder, 'arial.ttf'), 36)
        # get font size for center justification
        w, h = draw.textsize(guest, arial_font)
        # draw text of guest name
        draw.text(((360-w)/2, (203-h)/2), guest, fill='grey', font=arial_font)
        # save new image
        new_image.save(os.path.join('custom_seating_cards', f'{guest}_seating_card.png'))
