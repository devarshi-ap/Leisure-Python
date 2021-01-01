import imghdr
import smtplib
from email.message import EmailMessage

# turn on "google allow less secure apps - google account" <search on google> for the email sender and receiver
# theoretically, you could spam someone's inbox by looping the below code.

msg = EmailMessage()
msg['Subject'] = "Check out this radical pic Bro!"
msg['From'] = 'sender_email'
msg['To'] = 'receiver_email'
msg.set_content("Image attached...")


"""
uses open() and file PATH as argument to get info about file.

to send multiple files, make array of file PATHs strings & iterate thru it
via for loop and replace the x in open(x, r) with the loop variable.
"""

with open("file_PATH", "rb") as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)


# using smtp_ssl connection, you can remove the ehlo() and starttls()
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('sender_email', 'sender_email_password')
    smtp.send_message(msg)
