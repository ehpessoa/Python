#! python3
# regex_search.py - Opens all .txt files in a folder and searches for any line that matches a user-supplied RE.
# Prints results to screen.
# Usage: python regex_search.py <abs dir path> <user supplied regex>

import re
import sys
import os

# gets list of all .txt in a folder
working_dir = sys.argv[1]

# user supplied regex
user_regex = re.compile(sys.argv[2])

# loops through all files in dir looking for .txt files
for file in os.listdir(working_dir):
    if file.endswith('.txt'):
        with open(os.path.join(working_dir, file), 'r') as temp_file:
            temp_text = temp_file.read()
            # if there are matches to the regex, print all matches
            if user_regex.findall(temp_text):
                [print(f'{file}: {match}') for match in user_regex.findall(temp_text)]
