# Sending texts with python

#Imports
import twilio
print(twilio.__version__)

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6ea0b3c69aa2fd6f7c19d467283f1e78"
# Your Auth Token from twilio.com/console
auth_token  = "6769d73dedf3f1334580254e9209fe90"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14195756982",
    from_="+15673013579",
    body="My name is Ron Burgandy")

print(message.sid)

