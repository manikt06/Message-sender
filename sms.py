from twilio.rest import Client

account_sid = 'XYZ'#twilio account_sid
auth_token = 'ABC'#twilio auth_token
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='12345678',#enter your twilio account number here
  body='This is your message',#enter your message here
  to='87655'#enter your target phone number here
)

print(message.sid)