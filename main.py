import flaskSkill
import lightControl
import RPi.GPIO as GPIO
from time import sleep
from adafruit_motorkit import MotorKit
from flask import Flask, g
from flask_ask import Ask, statement
import os
from multiprocessing import Process, Value

resistorPin = 4

GPIO.setup(resistorPin, GPIO.OUT)
GPIO.output(resistorPin, GPIO.LOW)
sleep(0.1)
    
GPIO.setup(resistorPin, GPIO.IN)

kit = MotorKit()

app = Flask(__name__)
ask = Ask(app, '/')

STATUSOPEN = ["open", "raise", "raised", "opened", "up"]
STATUSCLOSED = ["close", "closed", "lower", "lowered", "down"]
closed = Value('i', 1)

light_process = Process(target=lightControl.lightMotor)   #, args=(closed))
alexa_process = Process(target=flaskSkill.main)    #, args=(closed))

light_process.start()
alexa_process.start()
