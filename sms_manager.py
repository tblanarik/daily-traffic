from twilio.rest import Client


class SMSManager:
    """Represents the everything needed to send a text message."""

    def __init__(self, twilio_account_sid, twilio_auth_token, to_phone_number, from_phone_number):
        self.twilio_account_sid = twilio_account_sid
        self.twilio_auth_token = twilio_auth_token
        self.to_phone_number = to_phone_number
        self.from_phone_number = from_phone_number

    def send_text_message(self, message_body):
        """Send text message with message body"""
        client = Client(self.twilio_account_sid, self.twilio_auth_token)
        client.messages.create(
            body=message_body,
            from_=self.from_phone_number,
            to=self.to_phone_number)
