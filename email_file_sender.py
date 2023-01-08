import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

def send_email(to, file_path):
    # create message object instance
    msg = MIMEMultipart()

    # setup the parameters of the message
    password = "uywmtwwxnncapoxb"
    msg['From'] = "anonmusk5@gmail.com"
    msg['To'] = ", ".join(to) # convert the list of email addresses to a string
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
        server.login(msg['From'], password)
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

while True:
    # send the email
    send_email(to=["darwaipranav@gmail.com"], file_path="/home/cipher/ai_tools/log.txt")
    time.sleep(24 * 60 * 60)

