import smtplib

# turn on "google allow less secure apps - google account" <search on google> for the email sender and receiver
# theoretically, you could spam someone's inbox by looping the below code.

# 'with' removes the need to close a smtp object
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    # identifies local to smtp
    smtp.ehlo()
    # encrypts traffic
    smtp.starttls()
    # reidentifies encrypted local
    smtp.ehlo()

    # email and password for gmail or yahoo or whtvr emailing service you use. This program is tailored for gmail
    smtp.login('sender_email', 'sender_email_password')

    subject = "Dat Nigerian Prince"
    body = "I'm sending this from a python script on pycharm. SMTP test!!!"
    msg = f'Subject: {subject}\n\n{body}'

    # (sender, receiver, message)
    smtp.sendmail('sender_email', 'receiver_email', msg)
