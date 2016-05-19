from flask import Flask, request
import json
import os

from googlevoice import voice
import sms

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receiveInfo():
    m = json.loads(request.data)
    phone = m['phone']
    text = m['text']
    print(phone + text)
    sms.newMsg(phone, text)
    return 'SUCCESS!'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
