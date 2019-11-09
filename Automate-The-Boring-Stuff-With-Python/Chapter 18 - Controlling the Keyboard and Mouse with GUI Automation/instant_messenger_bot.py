#! python3
# instant_messenger_bot.py - Clicks on friends in google hangouts and sends them a message

import pyautogui
import time

pyautogui.PAUSE = .25
pyautogui.FAILSAFE = True

# capture pictures of all recipients
friend_dict = {'friend_A': 'friend_A.PNG', 'friend_B': 'friend_B.PNG'}
# list of friends to msg
friend_list = ['friend_A', 'friend_B']
# msg
msg = 'sup homie this is a pyautogui test'

time.sleep(3)
for friend in friend_list:
    coords = pyautogui.locateOnScreen(friend_dict[friend])
    pyautogui.click(coords[0], coords[1])
    time.sleep(1)
    pyautogui.typewrite(msg)
    pyautogui.press('enter')
    time.sleep(3)
