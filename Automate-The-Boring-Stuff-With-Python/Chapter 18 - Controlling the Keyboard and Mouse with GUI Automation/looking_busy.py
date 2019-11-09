#! python3
# looking_busy.py - Nudges mouse every 10 seconds to prevent idleness

import pyautogui
import time

try:
    while True:
        print('Nudging mouse...')
        pyautogui.moveRel(1, 0)
        pyautogui.moveRel(-1, 0)
        print('Sleeping for 10 seconds\n')
        time.sleep(10)
except KeyboardInterrupt:
    print('Done.')
