import csv
import smtplib
import ssl
import getpass

message = """Subject: Your grade

Hi {name}, your grade is {grade}"""
smtp_server = "smtp.gmail.com"
port = 465
sender_email = "teste@gmail.com"
password = getpass.getpass(prompt='Password: ', stream=None)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    with open("./data/contacts_file.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, grade in reader:
            server.sendmail(
                sender_email,
                email,
                message.format(name=name, grade=grade),
            )
