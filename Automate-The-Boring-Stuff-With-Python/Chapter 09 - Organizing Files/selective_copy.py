#! python3
# selectiveCopy.py - walks through a folder tree and copies files with specific file extensions

import os
import shutil


def selective_copy(source_abs_fp, destination_abs_fp, file_extension):
    """
    Copies files matching file extension from source dir to destination dir
    :param source_abs_fp: String abs file path
    :param destination_abs_fp: String abs file path
    :param file_extension: String file extension
    :return: None
    """
    # get abs file path
    source_abs_fp = os.path.abspath(source_abs_fp)
    # walk through dir
    for current_folder, sub_folder_list, file_list in os.walk(source_abs_fp):
        # iter through file list
        for file in file_list:
            # if file matches extension, copy from current dir to source dir
            if file.endswith(file_extension):
                file_path = os.path.join(current_folder, file)
                new_path = os.path.join(destination_abs_fp, file)
                shutil.copy(file_path, new_path)
                print(f'Moving file...{file_path} to {new_path}')


selective_copy(r'C:\Users\Fox\Documents\Python', r'C:\Users\Fox\Documents\Python\logs', '.json')
