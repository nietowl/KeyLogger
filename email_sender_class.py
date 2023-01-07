import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, password, sender, recipients):
        self.password = password
        self.sender = sender
        self.recipients = recipients

    def send_email(self, file_path):
        # create message object instance
        msg = MIMEMultipart()

        # setup the parameters of the message
        msg['From'] = self.sender
        msg['To'] = ", ".join(self.recipients) # convert the list of email addresses to a string
        msg['Subject'] = "File Attachment"

        try:
            # open the file in bynary
            binary_pdf = open(file_path, 'rb')

            # attach the file
            part = MIMEApplication(binary_pdf.read(), Name=os.path.basename(file_path))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            msg.attach(part)
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
            return

        # create server
        server = smtplib.SMTP('smtp.gmail.com:587')

        server.starttls()

        try:
            # Login Credentials for sending the mail
            server.login(msg['From'], self.password)
        except smtplib.SMTPAuthenticationError:
            print("Error: Invalid login credentials")
            return

        try:
            # send the message via the server.
            server.sendmail(msg['From'], msg['To'], msg.as_string())
        except smtplib.SMTPException:
            print("Error: Unable to send email")
            return

        server.quit()

# create an instance of the EmailSender class
email_sender = EmailSender(password="uywmtwwxnncapoxb", sender="anonmusk5@gmail.com", recipients=["darwaipranav@gmail.com"])

# send the email
email_sender.send_email(file_path="/path/to/file.pdf")

send the email every 24 hours
while True:
    email_sender.send_email(file_path="/home/cipher/ai_tools/log.txt")
    time.sleep(24 * 60 * 60)
# email_sender.send_email(file_path="/home/cipher/ai_tools/log.txt")