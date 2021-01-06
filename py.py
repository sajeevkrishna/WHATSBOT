from flask import Flask,render_template,request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

app=Flask(__name__)


@app.route('/',methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    if('\n' in incoming_msg):
        client = Client('#SID TOKEN FOR TWILIO','AUTHENTICATION TOKEN FOR TWILIO')
        data=incoming_msg.splitlines()
        message = client.messages.create(from_='whatsapp:+14155238886',body=data[0],to='whatsapp:'+data[1])
        return ''
    else:
        resp = MessagingResponse()
        msg = resp.message()
        msg.body(incoming_msg)
        return str(resp)


if __name__ == "__main__":
    app.run(debug=True)