#! python3
# regexVersionOfStrip.py
# first argument is the string to search
# second argument default is whitespace, or whatever is entered

import re


def regex_strip(input_string, char_to_strip=None):
    """
    Mimics String.strip() method, default is whitespace at the ends
    Otherwise, strips the given chars
    :param input_string:
    :param char_to_strip:
    :return:
    """
    if char_to_strip:
        main_regex = re.compile(rf'{char_to_strip}')
    else:
        main_regex = re.compile(r'^\s|\s$')
    return main_regex.sub('', input_string)
