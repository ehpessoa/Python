#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import pyperclip
import shelve
import sys

if len(sys.argv) > 1:
    mcb_shelf = shelve.open('mcb')
    # check for save cmd
    if sys.argv[1].lower() == 'save':
            # save and list are invalid cmds
            if sys.argv[1].lower() == 'save' or sys.argv[1].lower() == 'list':
                print('Invalid Key - Cannot use <save> or <list>')
            # save clipboard under keyword
            else:
                mcb_shelf[sys.argv[2]] = pyperclip.paste()
    # check for list cmd, list all keys
    elif sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys)))
    # check for keyword
    elif sys.argv[1].lower() in mcb_shelf.keys():
        # copy saved text to clipboard
        pyperclip.copy(mcb_shelf[sys.argv[1]])
    else:
        print('Cmd or keyword not recognized.')
    mcb_shelf.close()
