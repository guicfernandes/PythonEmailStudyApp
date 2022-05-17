from email_sender import EmailSender
import getpass


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "teste@gmail.com"
receiver_email = "teste@msn.com"

simple_message = """\
Subject: Hi there

This message is sent from Python."""

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""
subject = "Multipart test"

subject_attach = "An email with attachment from Python"
body_attach = "This is an email with attachment sent from Python"
file_name_attach = "./data/Dont-Say-The-Words-Jobs.pdf"

sender = EmailSender(port, smtp_server)
sender.set_email_params(
    sender_email,
    getpass.getpass(prompt='Password: ', stream=None),
    receiver_email
)
# sender.set_simple_message(simple_message)
#sender.set_mime_plain_html_message(text, html, subject)
sender.set_mime_multipart_message(
    subject_attach, body_attach, file_name_attach)
sender.send_email()
