# twilio trial phone number: +19378723690

from twilio.rest import Client

account_sid = "AC5cade0d7afb7954ba1d090265ffc5841"
auth_token  = "180c61e80bc9c4daa27733c71d03b9c5"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body  = "This is sent from Python",
    from_ = "+19378723690",
    to    = ("+919474158862"),
)

print(message.sid)
