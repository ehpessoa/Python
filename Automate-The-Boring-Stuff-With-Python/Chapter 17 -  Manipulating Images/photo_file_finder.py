#! python3
# photo_file_finder.py - Walks through path to look for photo folders

import os
from PIL import Image

path = r'C:\Users\Fox\Downloads'

# walk through C drive
for dir_folder, sub_folders, file_names in os.walk(path):
    # init counters for photos, non-photos
    photo_count = 0
    non_photo_count = 0
    # check files for photo - jpg and png are photos
    for file in file_names:
        if not (file.lower().endswith('.png') or file.lower().endswith('.jpg')):
            non_photo_count += 1
            continue
        else:
            # check for pixel width and height greater than 1000
            try:
                # print(os.path.join(dir_folder, file))
                open_file = Image.open(os.path.join(dir_folder, file))
                file_width, file_height = open_file.size
                if file_width < 500 or file_height < 500:
                    non_photo_count += 1
                    continue
                else:
                    photo_count += 1
            except FileNotFoundError:
                print(f'File not found: {file}')
                continue
    # if more than 50% of the files are pictures, print abs folder
    if photo_count > non_photo_count:
        print(dir_folder)
