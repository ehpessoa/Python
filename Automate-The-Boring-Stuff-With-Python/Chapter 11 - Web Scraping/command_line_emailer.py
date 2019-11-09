#! python3
# commandLineEmailer.py - logs into gmail and sends an email

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

myEmail = 'someEmail@gmail.com'
emailPassword = 'abcPassword'

targetEmail = 'xyz@gmail.com'
subjectString = 'shitty email incoming'
msgString = 'iSukAtCoding.kthxbye'

# opens gmail page
browser = webdriver.Firefox()
browser.get('https://www.gmail.com')
# sets default wait to 10 seconds
wait = WebDriverWait(browser, 10)

# login, by name
wait.until(expected_conditions.presence_of_element_located((By.NAME, 'identifier')))
browser.find_element_by_name('identifier').send_keys(myEmail, Keys.ENTER)

# wait until password entry comes into view, by name
wait.until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
browser.find_element_by_name("password").send_keys(emailPassword)

# find compose new email button and open, by xpath
elem_xpath = '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div'
wait.until(expected_conditions.presence_of_element_located((By.XPATH, elem_xpath)))
browser.find_element_by_xpath(elem_xpath).click()

# input the recipient, subject, msg body, by ID
wait.until(expected_conditions.presence_of_element_located((By.ID, ':170')))
browser.find_elements_by_id(':170').send_keys(targetEmail)
browser.find_elements_by_id(':16j').send_keys(subjectString)
browser.find_elements_by_id(':17n').send_keys(msgString)

# send! by id
wait.until(expected_conditions.presence_of_element_located((By.ID, ':1kg')))
browser.find_elements_by_id(':1kg').click()
