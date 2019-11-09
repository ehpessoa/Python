#! python3
# mad_libs.py - replaces ADJ, VERB, NOUN in sentence with user supplied inputs
# Usage: python mad_libs.py <text file abs path>

import sys
import re

# open target text file and read text
with open(sys.argv[1], 'r') as txt_file:
    original_txt = txt_file.read()
    txt = re.findall(r"[\w']+|[.,!?;]", original_txt)
    # open index or choose the word
    for word in txt:
        # check for match and replace with user input
        if word == 'ADJECTIVE':
            user_input = input('Enter an adjective: ')
            original_txt = original_txt.replace('ADJECTIVE', user_input, 1)
            # this also works but i prefer the string method over the re module
            # original_txt = re.sub('ADJECTIVE', user_input, original_txt, 1)
        elif word == 'NOUN':
            user_input = input('Enter a NOUN: ')
            original_txt = original_txt.replace('NOUN', user_input, 1)
        elif word == 'VERB':
            user_input = input('Enter a VERB: ')
            original_txt = original_txt.replace('VERB', user_input, 1)
    # save new file
    with open('new_file.txt', 'w') as new_file:
        new_file.write(original_txt)
