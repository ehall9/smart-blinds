from flask import Flask, g
from flask_ask import Ask, statement
import os
from time import sleep
import RPi.GPIO as GPIO
from adafruit_motorkit import MotorKit

kit = MotorKit()

app = Flask(__name__)
ask = Ask(app, '/')

STATUSOPEN = ["open", "raise", "raised", "opened", "up"]
STATUSCLOSED = ["close", "closed", "lower", "lowered", "down"]

@ask.intent('HelloWorldIntent')
def hello():
    speech_text = "Hello"
    return statement(speech_text).simple_card('Hello', speech_text)

@ask.intent('BlindsIntent', mapping = {'status':'status'})
def Blinds_Intent(status, room):
    if status in STATUSOPEN:
        # if g.closed.value == 1:
        kit.motor1.throttle = 1
        sleep(7)
        kit.motor1.throttle = 0
            # g.closed.value = 0
        return statement('Opening The Blinds')
        # else:
        #     return statement('Blinds Are Already Open')
    if status in STATUSCLOSED:
        # if g.closed.value == 0:
        kit.motor1.throttle = -1
        sleep(6.3)
        kit.motor1.throttle = 0 
            # g.closed.value = 1
        return statement('Closing The Blinds')
        # else:
        #     return statement('Blinds Are Already Closed')

@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'EAT SHIT'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)

@ask.session_ended
def session_ended():
    return "{}", 200

def main():  #closed):
    #g.closed = closed
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)

if __name__ == '__main__':
    main()