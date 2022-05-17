import smtplib
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailSender:
    """Send emails"""

    def __init__(self, port, smtp_server):
        self.port = port
        self.smtp_server = smtp_server
        # Create a secure SSL context
        self.context = ssl.create_default_context()

    def set_email_params(self, sender, sender_pass, receiver):
        self.sender_email = sender
        self.sender_pass = sender_pass
        self.receiver_email = receiver

    def set_simple_message(self, message):
        self.message = message

    def set_mime_plain_html_message(self, plain_text, html_text, subject):
        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = subject
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(plain_text, "plain")
        part2 = MIMEText(html_text, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        self.message.attach(part1)
        self.message.attach(part2)
        self.message = self.message.as_string()

    def read_pdf_file(self, file_name):
        # Open PDF file in binary mode
        with open(file_name, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        return part

    def add_file(self, file_name):
        part = self.read_pdf_file(file_name)
        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {file_name}",
        )

        # Add attachment to message and convert message to string
        self.message.attach(part)
        self.message = self.message.as_string()

    def set_mime_multipart_message(self, subject, body, file_name):
        # Create a multipart message and set headers
        self.message = MIMEMultipart()
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email
        self.message["Subject"] = subject
        # Recommended for mass emails
        self.message["Bcc"] = self.receiver_email
        # Add body to email
        self.message.attach(MIMEText(body, "plain"))
        self.add_file(file_name)

    def send_email(self):
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=self.context) as server:
            server.login(self.sender_email, self.sender_pass)
            server.sendmail(self.sender_email,
                            self.receiver_email, self.message)
