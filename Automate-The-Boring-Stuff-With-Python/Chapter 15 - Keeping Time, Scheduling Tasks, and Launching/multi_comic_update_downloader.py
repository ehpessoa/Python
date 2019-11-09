#! python 3
# multi_comic_update_downloader.py - Checks for updates for XKCD and Cyanide&Happiness and downloads
"""
For crontab scheduling (linux):
0 0 0 0 0 /path/to/python /path/to/multi_comic_update_downloader.py
"""

import os
import bs4
import json
import requests
from requests.exceptions import HTTPError

os.makedirs('Comics', exist_ok=True)


# XKCD comic checker
def xkcd_updater(xkcd_comic_num):
    test_comic_num = xkcd_comic_num
    print('Checking xkcd...')
    while True:
        try:
            # hard code url
            url = f'https://xkcd.com/{test_comic_num}/'
            # if no 404, download
            xkcd_html = requests.get(url)
            xkcd_html.raise_for_status()
            soup = bs4.BeautifulSoup(xkcd_html.text, 'lxml')
            # set new_url to the image link
            new_url = 'http:' + soup.select('#comic img')[0]['src']
            # download new_url, because new url uses a name and not a comic number
            new_req = requests.get(new_url)
            try:
                # check if comic downloaded successfully
                new_req.raise_for_status()
                # save comic
                with open(os.path.join('Comics', os.path.basename(new_url)), 'wb') as new_comic:
                    for chunk in new_req.iter_content(10000):
                        new_comic.write(chunk)
                    print(f'Saved xkcd comic # {test_comic_num} - {os.path.basename(new_url)}')
                    # append by 1 to download next comic
                    test_comic_num += 1
            except HTTPError:
                # stop when 404 error
                print(f'Comic #{test_comic_num} exists but comic image url not valid')
        # input proper exception
        except HTTPError:
            if test_comic_num == xkcd_comic_num:
                print(f'Comic not yet updated. Comic #{xkcd_comic_num - 1} is the latest comic.')
            else:
                print(f'No further comics after {test_comic_num - 1}.')
            # save latest comic number
            return test_comic_num - 1


# Cyanide&Happiness checker
def cyanide_happiness_updater(ch_comic_num):
    test_comic_num = ch_comic_num
    print('Checking Cyanide&Happiness...')
    while True:
        try:
            # hard code url
            url = f'http://explosm.net/comics/{test_comic_num}/'
            comic_html = requests.get(url)
            # parsing the html
            soup = bs4.BeautifulSoup(comic_html.text, 'lxml')
            # select the img src
            comic_src = soup.select('#main-comic')[0]['src']
            # set new url link to img src, because comic uses name and not a number
            new_url = f'http:{comic_src}'
            try:
                # request the new url
                new_req = requests.get(new_url)
                new_req.raise_for_status()
                # remove '?' from basename to save acceptable file name
                if os.path.basename(new_url).split('?', 1)[0]:
                    comic_name = os.path.basename(new_url).split('?', 1)[0]
                else:
                    comic_name = os.path.basename(new_url)
                # save the new comic
                with open(os.path.join('Comics', comic_name), 'wb') as new_comic:
                    for chunk in new_req:
                        new_comic.write(chunk)
                    print(f'Comic #{test_comic_num} downloaded.')
                # advance to next comic num
                test_comic_num += 1
            except HTTPError:
                print(f'Comic #{test_comic_num} exists but comic image url not valid')
        except (HTTPError, IndexError):
            if test_comic_num == ch_comic_num:
                print(f'Comic not yet updated. Comic #{test_comic_num - 1} is the latest comic.')
            else:
                print(f'No further comics after {test_comic_num - 1}.')
            # returns latest comic number
            return test_comic_num - 1


# load json for dictionary of key comic, latest comic number
with open('comic.json', 'r') as comic_json:
    # load json
    comic_info = json.load(comic_json)
    # advance the latest comic numbers + 1
    xkcd_num = int(comic_info['XKCD']) + 1
    ch_num = int(comic_info['CH']) + 1

    # call xkcd_updater
    new_xkcd_num = xkcd_updater(xkcd_num)
    # call ch_updater
    new_ch_num = cyanide_happiness_updater(ch_num)

# if comics were downloaded, update new comic to most recent comic number
# failed comic download - 1
if new_xkcd_num > xkcd_num or new_ch_num > ch_num:
    comic_info['XKCD'] = new_xkcd_num
    comic_info['CH'] = new_ch_num
    with open('comic.json', 'w') as comic_json:
        json.dump(comic_info, comic_json)
