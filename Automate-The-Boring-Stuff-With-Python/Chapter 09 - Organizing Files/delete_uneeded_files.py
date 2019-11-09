#! python3
# delete_unneeded_files.py - searches for files or folders over a certain size in target directory

import os


def recurse_find_folder_size(target_directory, file_size):
    """
    Recursively iterates through a directory and checks for over-sized files and subdirectories. Prints them.
    :param target_directory: String abs path of directory
    :param file_size: Int file size threshold
    :return: Total size of the directory
    """
    total_size = 0
    # walk through dir
    for item in os.listdir(target_directory):
        # convert item to file path
        item_fp = os.path.join(target_directory, item)
        # if file, add to total_size
        if os.path.isfile(item_fp):
            total_size += os.path.getsize(item_fp)
            # print if file is over file_size
            if os.path.getsize(item_fp) > file_size:
                print(item_fp, os.path.getsize(item_fp))
        # if dir, recurse
        elif os.path.isdir(item_fp):
            total_size += recurse_find_folder_size(item_fp, file_size)
    # if total size of folder > file_size, return. Also works for subdirectories when recursing
    if total_size > file_size:
        print(target_directory, total_size)
    return total_size


# Print out the total size of the target directory
print('Total size: ' + str(recurse_find_folder_size(
    r"C:\Users\Fox\Documents\Python\Automate-The-Boring-Stuff-With-Python", 4000)))
