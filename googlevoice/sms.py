from googlevoice import Voice
from googlevoice.util import input

voice = Voice()
voice.login()

def newMsg(phone, text):
    voice.send_sms(phone, text)
