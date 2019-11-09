#! python3
# 2048.py - Plays 2048 with basic up, right, down, left

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# hardcoded url
url = 'https://gabrielecirulli.github.io/2048/'
# start browser and get url, maximize window
browser = webdriver.Firefox()
browser.get(url)
browser.maximize_window()

# can only send_key after selecting the whole HTML
window = browser.find_element_by_tag_name('html')

# set up the lists for iterating
directional_keys = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]

# loop until list returned by class name has a node obj
while not browser.find_elements_by_class_name('game-over'):
    # loop through directional keys
    for key_press in directional_keys:
        window.send_keys(key_press)
