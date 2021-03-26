import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv("C:/data/.env")

account_sid = os.getenv("TWI_ACC_SID")
auth_token = os.getenv("TWI_AUTH_TOK")
twilio_from = os.getenv("TWI_FROM_NUM")
twilio_to = os.getenv("TWI_TO_NUM")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=twilio_from,
            to=twilio_to
        )
        print(message.sid)