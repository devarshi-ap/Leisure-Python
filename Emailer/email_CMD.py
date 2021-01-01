"""
In the terminal, type --> python3 -m smtpd -c DebuggingServer -n localhost:1025
This starts a debug server which will receive any messages sent to localhost 1025 then discard it

After typing the top part in, run the code. It will show the message in the terminal window
"""
import smtplib


with smtplib.SMTP('localhost', 1025) as smtp:

    subject = "What's gwannin shordy"
    body = "SMTP test!!!"
    msg = f'Subject: {subject}\n\n{body}'

    # (sender, receiver, message)
    smtp.sendmail('devarshi.ap@gmail.com', 'crownthebat@gmail.com', msg)
