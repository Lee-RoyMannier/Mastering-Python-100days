import os

from dotenv import load_dotenv
import smtplib
load_dotenv()


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.login = os.environ['LOGIN_MAIL']
        self.password = os.environ['PASSWORD_MAIL']

    def send_emails(self, mail_users, message):
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(self.login, self.password)
            smtp.sendmail(
                to_addrs=mail_users,
                from_addr=self.login,
                msg=message
            )
