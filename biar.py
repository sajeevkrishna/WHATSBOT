from twilio.rest import Client
client = Client('ACc2a04dff25d3d3e1ce5de37d19bf2df3','1ea8c48816801e9a4ecfd49cf440c866')
str='this is the virtual internship presentaion'
message = client.messages.create(from_='whatsapp:+14155238886',body=str,to='whatsapp:+919361217536')
