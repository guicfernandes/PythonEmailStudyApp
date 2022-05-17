import smtplib
import ssl
import getpass

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "teste@gmail.com"
receiver_email = "teste@gmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""


#password = input("Type your password and press enter: ")
password = getpass.getpass(prompt='Password: ', stream=None)

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
