import os
import time
import time
import datetime
from colorama import *
from art import *
import smtplib #optional advanced
from email.mime.multipart import * # optional and advanced
from email.mime.text  import * # optional and advanced
from email.message import EmailMessage


init()

#email function  (optional & advanced)
def gmail_send(subject, message, from_mail, to_mail, password):
    global link
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_mail, password)
    msg            = EmailMessage()
    message        = f'{message}'
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From']    = from_mail
    msg['To']      = to_mail
    server.send_message(msg)

new_entry = input("Enter diary entry here:   ")

now = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
print(now)

with open("copy.txt", "a") as file:
    file.write(now + " " + new_entry + "\n")

