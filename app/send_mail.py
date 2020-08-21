import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

from flask import Flask

app = Flask(__name__)

from config import MAIL, PASS, mail_to, subject


def send_email(mail_to, subject, text):
    try:
        assert isinstance(mail_to, list)
        smtp_user = MAIL
        smtp_pwd = PASS
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = COMMASPACE.join(mail_to)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject

        msg.attach(MIMEText(text, 'html'))

        smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp.ehlo()
        smtp.login(smtp_user, smtp_pwd)
        smtp.sendmail(smtp_user, mail_to, msg.as_string())
        smtp.close()
        print(msg)
        return True

    except Exception as e:
        print(e, 'error')
        return False



