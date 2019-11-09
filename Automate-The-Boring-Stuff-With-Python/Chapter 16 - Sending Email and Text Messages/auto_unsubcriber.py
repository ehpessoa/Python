#! python3
# auto_unsubscriber.py - logs onto email and checks 5 most emails for unsub links

import imaplib
import email
import bs4
import webbrowser

email_address = 'email@gmail.com'
password = 'sekrit_pw'

# login to IMAP server
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(user=email_address, password=password)
mail.select('INBOX')
result, data = mail.uid('search', None, "ALL")
# split up emails in inbox, convert to list
inbox_item_list = data[0].split()

# checks 5 most recent emails, modify this if you want all emails
for email_num in range(-5, 0):
    # get first result in inbox, encoded
    result, email_data = mail.uid('fetch', inbox_item_list[email_num], '(RFC822)')
    # decode email into string
    raw_email = email_data[0][1].decode('utf-8')
    # parse string using email module
    email_message = email.message_from_string(raw_email)

    # walk through each part of email until not multipart
    for part in email_message.walk():
        if not part.is_multipart():
            # decode and retrieve email body in html
            payload = part.get_payload(decode=True)
            # parse html
            soup = bs4.BeautifulSoup(payload, 'lxml')
            # opens each link with unsub text in webbrowser
            for link in soup.find_all(href=True, text='Unsubscribe'):
                webbrowser.open(link.get('href'))

mail.logout()
