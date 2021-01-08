import os
import smtplib
from email.message import EmailMessage

email_id = 'exampleMail1@gmail.com'
email_pass = 'passwordHere'

recipient_list = ['exampleMail2@gmail.com', 'exampleMail3@gmail.com','exampleMail4@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'first mail using python'
msg['From'] = email_id
msg['To'] = recipient_list
msg.set_content('how about a movie tonight')

for each_file in os.listdir():
    if each_file == 'pymail.py':
        continue
    with open(each_file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_id, email_pass)
    smtp.send_message(msg)
