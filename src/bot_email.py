import smtplib
from email.mime.text import MIMEText

from dotenv import dotenv_values

config: dict = dotenv_values(".env")
EMAIL_ADRESS = str(config["EMAIL_ADRESS"])
PASSWORD = str(config["PASSWORD"])


def send_email(message, *args):
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(EMAIL_ADRESS, PASSWORD)
        msg = MIMEText(message)
        msg["Subject"] = f"NEW TEST! from {args}"
        server.sendmail(EMAIL_ADRESS, EMAIL_ADRESS, msg.as_string())
        server.quit()
        print("The message was sent successfully!")  # just for checking
    except Exception as _ex:
        print(f"{_ex}\nCheck your login or password please!")  # just for checking
