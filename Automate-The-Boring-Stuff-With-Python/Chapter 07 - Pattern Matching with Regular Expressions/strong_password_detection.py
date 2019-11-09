#! python3
# strongPasswordDetection.py - checks password and returns whether strong or not

import re

test_string = input('Enter your password.')

upper_regex = re.compile(r'[A-Z]')
lower_regex = re.compile(r'[a-z]')
num_regex = re.compile(r'\d')


def password_strength(input_string):
    """
    Checks input_string for strength
    :param input_string: String password
    :return: Boolean
    """
    # check len
    if len(test_string) < 8:
        print('Password is less than 8 characters.')
        return False
    # check upper
    if not upper_regex.search(input_string):
        print('Password has no uppercase character.')
        return False
    # check lower
    if not lower_regex.search(input_string):
        print('Password has no lowercase character.')
        return False
    # check number
    if not num_regex.search(input_string):
        print('Password has no number character.')
        return False
    print('Secure password.')
    return True
