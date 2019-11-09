#! python3
# fillingInTheGaps.py

# finds and locates gaps in numbering, assume no misnamed files such as spam1 vs spam001

import os
import re
import shutil


def fill_in_gaps(abs_path, prefix):
    # get abs path for absPath
    abs_path = os.path.abspath(abs_path)
    # number matching regex
    num_regex = re.compile(rf'({prefix})?(\d+)(\.\w+)')
    # get list of files in folder
    files = [file for file in os.listdir(abs_path)
             if num_regex.match(file) and os.path.isfile(os.path.join(abs_path, file))]

    # sort function key
    def regex_sort(file_name):
        """
        Function for use as a key in sorting files by regex numbers
        :param file_name: String
        :return: Int numbers of file (mo.group(2))
        """
        mo = num_regex.search(file_name)
        return int(mo.group(2))

    # sort files based on key
    files.sort(key=regex_sort)
    # search for longestNum
    starting_num = num_regex.search(files[0]).group(2)
    # pad the numbers so the all the numbers will be the same length
    padding = max([len(num_regex.search(file).group(2)) for file in files])
    current_number = str(starting_num).rjust(padding, '0')

    # iter through sorted files and if file num does not match the current_number, rename
    for file in files:
        if num_regex.search(file).group(2) != current_number:
            # renames files by moving them with new name
            shutil.move(os.path.join(abs_path, file),
                        f'{abs_path}\{prefix}{current_number}{num_regex.search(file).group(3)}')
            print(f'new file name: {abs_path}\{prefix}{current_number}{num_regex.search(file).group(3)}')
        # iterate from current number by adding 1
        current_number = (str(int(current_number) + 1)).rjust(padding, '0')


# implement gap by skipping current_number if == gap
def make_gaps(abs_path, prefix, gap_position, gap_num):
    # make new dir for moving files because some files can get overridden
    os.makedirs('new_files', exist_ok=True)
    dir_path = os.path.abspath('new_files')
    # get abs path for absPath
    abs_path = os.path.abspath(abs_path)
    # number matching regex
    num_regex = re.compile(rf'({prefix})?(\d+)(\.\w+)')
    # get list of files in folder
    files = [file for file in os.listdir(abs_path)
             if num_regex.match(file) and os.path.isfile(os.path.join(abs_path, file))]

    # sort function key
    def regex_sort(file_name):
        """
        Function for use as a key in sorting files by regex numbers
        :param file_name: String
        :return: Int numbers of file (mo.group(2))
        """
        mo = num_regex.search(file_name)
        return int(mo.group(2))

    # sort files based on key
    files.sort(key=regex_sort)
    # search for longestNum
    starting_num = num_regex.search(files[0]).group(2)
    # pad the numbers so the all the numbers will be the same length
    padding = max([len(num_regex.search(file).group(2)) for file in files])
    current_number = str(starting_num).rjust(padding, '0')

    # iter through sorted files, create files that fit gap
    for file in files:
        if gap_position == int(current_number):
            current_number = int(current_number) + gap_num
            current_number = str(current_number).rjust(padding, '0')
        if num_regex.search(file).group(2) != current_number:
            # renames files by moving them with new name
            shutil.move(os.path.join(abs_path, file),
                        f'{dir_path}\{prefix}{current_number}{num_regex.search(file).group(3)}')
            #             f'{abs_path}\{prefix}{current_number}{num_regex.search(file).group(3)}')
            print(f'new file name: new_files\{prefix}{current_number}{num_regex.search(file).group(3)}')
        # iterate from current number by adding 1
        current_number = (str(int(current_number) + 1)).rjust(padding, '0')

        
# fill_in_gaps(r'C:\Users\Fox\Documents\Python\logs', 'spam')
# make_gaps(r'C:\Users\Fox\Documents\Python\logs', 'spam', 1, 2)
