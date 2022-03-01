from twilio.rest import Client


class Mailer:

    def __init__(self, receiver):
        self.sid = "ACdcbccef757b3123bbaa9ed88b9aae82e"
        self.token = "576f8c3cd4c0dfba6e8644c118547293"
        self.receiver = receiver
        self.sender = "+19206268558"


    def sendmail(self, message):
        client = Client(self.sid, self.token)
        client.messages.create(body=message, from_=self.sender, to=self.receiver)
