# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC104f4db6eef785d68e8024fb8265a911'
auth_token = 'dd3cb8c2eef453d8952a7084b8d4438c'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+33644601945',
                     to='+237694913221'
                 )

print(message.sid)
