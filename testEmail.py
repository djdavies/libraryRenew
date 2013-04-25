#!/usr/bin/python
import smtplib
import datetime
now = datetime.datetime.now()

# these are for gmail, change them if you use something else
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'senderEmail@senderEmail.com' # change this
password = 'your email password'
recipient = 'recipient@recipientEmail.com' # change this
subject = 'You have renewed your library books'
body = 'sent from cfhack 2013. books renewed on: ' # change this. Updates will be sending book titles and dates

"Sends an e-mail to the specified recipient."

body = "" + body + "" + now.strftime("%Y-%m-%d %H:%M") + "\n\n--Regards\nLibrary Rewenal Bot\n"

headers = ["From: " + sender,
    "Subject: " + subject,
    "To: " + recipient,
    "MIME-Version: 1.0",
    "Content-Type: text/html"]
headers = "\r\n".join(headers)

# again, for gmail, change if you use something else
session = smtplib.SMTP('smtp.gmail.com', 587)

session.ehlo()
session.starttls()
session.ehlo
session.login(sender, password)

session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
session.quit()
