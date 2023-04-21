import requests

class MessageManager:
    """Sends a message to a POST endpoint"""
    def __init__(self, post_url):
        self.post_url = post_url

    def send_message(self, message, recipients):
        """Send message to POST endpoint"""
        requests.post(self.post_url, json={"message": message, "recipients": recipients}, timeout=30)