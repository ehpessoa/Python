#!python3
# umbrella_reminder.py - checks https://www.weather.gov and sends sms if raining.

import requests
import bs4
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'some_account_sid'
auth_token = 'some_auth_token'
client = Client(account_sid, auth_token)

twilio_num = '+123456789'
my_num = '+123456789'


def text_myself(message):
    """
    :param message: String message
    :return: SID for sent message
    """
    sms = client.messages.create(
        body=message,
        from_=twilio_num,
        to=my_num)
    return sms.sid


# request weather html
req = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.6366&lon=-73.993')
# parse html with beautifulsoup
soup = bs4.BeautifulSoup(req.text, 'lxml')
# select p node with class myforecast-current, select first obj in list
forecast = soup.select(selector='p.myforecast-current')[0].text

# look for rain or showers in forecast and text result
if 'rain' in forecast.lower() or 'showers' in forecast.lower():
    text_myself(f'Forecase is {forecast}. Bring an umbrella.')
else:
    text_myself(f'Forecast is {forecast}')
