#! python3
# random_chore_assignment_emailer.py - reads last week's chores and emails new chores

import random
import json
import smtplib

# smtp google info
my_email = 'self@gmail.com'
my_password = 'secret_password'

# recipient addresses and chores
email_addresses = ['one@email.com', 'two@email.com', 'three@email.com', 'four@email.com']
chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']

# open txt file with last week's chores in a dict
with open('last_week_chores.json', 'r') as last_week_chores_text:
    last_week_chores = json.load(last_week_chores_text)
    this_week_chores = {}

    # randomly assign chores, remove after assignment
    while True:
        temp_chore_list = chores[:]
        for email in email_addresses:
            selected_chore = random.choice(temp_chore_list)
            this_week_chores[email] = selected_chore
            temp_chore_list.remove(selected_chore)
        # check for repeats from prior week by checking if there is any overlap
        if not this_week_chores.items() & last_week_chores.items():
            break
    
    # login to SMTP server
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(my_email, my_password)

    # email new chore list to recipients
    for recipient_email, chore in this_week_chores.items():
        smtpObj.sendmail(from_addr=email_addresses, to_addrs=recipient_email,
                         msg=f'Subject: Test.\n{chore}')

# save this week's chores
with open('last_week_chores.json', 'w') as last_week_chores_update:
    json_file = json.dump(this_week_chores, last_week_chores_update, indent=2)
