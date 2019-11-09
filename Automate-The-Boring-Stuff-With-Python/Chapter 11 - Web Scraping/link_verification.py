#! python3
# linkVerifier.py - checks given url for broken links. If the url is JS heavy, probably should use selenium or other.

import requests
import bs4
import pprint

# hard coded url without trailing /
url = 'https://darksky.net'
# url = 'https://www.reddit.com/r/all'
urlRequest = requests.get(url)
urlRequest.raise_for_status()

# parse the link with bs4
soup = bs4.BeautifulSoup(urlRequest.text, 'lxml')
link_list = soup.find_all(href=True)

if link_list:
    broken_links = []
    for link in link_list:
        # javascript rendering, won't count this as broken link, use selenium for JS testing
        if link.get('href') == 'None':
            continue
        # get root url and check
        if link.get('href').startswith('/'):
            if requests.get(url + link.get('href')).status_code == 404:
                broken_links.append(link.get('href'))
        # get root url and check
        else:
            if requests.get(link.get('href')).status_code == 404:
                broken_links.append(link.get('href'))
    print(f'Total HREF {len(link_list)}')
    print(f'Total Broken HREF {len(broken_links)}')
    print('\nBroken links:')
    pprint.pprint(broken_links)
else:
    print('No links detected.')
