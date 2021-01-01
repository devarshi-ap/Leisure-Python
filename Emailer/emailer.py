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

    # my email and password
    smtp.login('devarshi.ap@gmail.com', 'Mahadev1109')

    subject = "Dat Nigerian Prince"
    body = "I'm sending this from a python script on pycharm. SMTP test!!!"
    msg = f'Subject: {subject}\n\n{body}'

    # (sender, receiver, message)
    smtp.sendmail('devarshi.ap@gmail.com', 'crownthebat@gmail.com', msg)
