#! python3
# image_site_downloader.py - Uses selenium to scrape imgur for download links

import os
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

os.makedirs('imgur', exist_ok=True)

search_term = 'ethereum'
url = 'https://imgur.com'
category_url = f'{url}/search?q={search_term}'

# launch browser and time out javascript, otherwise it will run too long
fp = webdriver.FirefoxProfile()
fp.set_preference("http.response.timeout", 3)
fp.set_preference("dom.max_script_run_time", 3)
browser = webdriver.Firefox(firefox_profile=fp)

# get initial top images
browser.get(category_url)
WebDriverWait(browser, 15).until(ec.element_to_be_clickable((By.CLASS_NAME, 'image-list-link')))
image_links = [x.get_attribute('href') for x in browser.find_elements_by_class_name('image-list-link')]

# $x('div[class="post-image-container"//descendant::[@src]')
copy = image_links[:]
for image_page in image_links:
    # get url and wait for loading
    browser.get(image_page)
    WebDriverWait(browser, 15).until(ec.visibility_of_element_located((By.CLASS_NAME, 'post-image-container')))
    # find mp4 gifs first
    if browser.find_elements_by_xpath('//div[@class="video-container"]//source'):  # video
        direct_image = browser.find_elements_by_xpath('//div[@class="video-container"]//source')
        direct_image_link = direct_image[0].get_attribute('src').replace('.mp4', '.gif')
    # find image type
    elif browser.find_elements_by_xpath('//a[@class="zoom"]//*'):
        direct_image = browser.find_elements_by_xpath('//a[@class="zoom"]//*')
        direct_image_link = direct_image[0].get_attribute('src')
    # find other image type
    elif browser.find_elements_by_xpath('//div[@class="image post-image"]//*'):
        direct_image = browser.find_elements_by_xpath('//div[@class="image post-image"]//*')
        direct_image_link = direct_image[0].get_attribute('src')
    else:
        # defaults
        print('NONE FOUND!!')
        direct_image_link = ''
    # print image url
    print(direct_image_link)
    direct_image_link = direct_image_link.split('?')[0]
    # download image
    file_request = requests.get(direct_image_link, stream=True)
    with open(os.path.join('imgur', os.path.basename(direct_image_link)), 'wb') as file:
        for chunk in file_request.iter_content(10000):
            file.write(chunk)
