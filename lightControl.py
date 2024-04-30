import RPi.GPIO as GPIO
from time import sleep
from adafruit_motorkit import MotorKit

def lightMotor(): #closed): 
   resistorPin = 4

   GPIO.setup(resistorPin, GPIO.OUT)
   GPIO.output(resistorPin, GPIO.LOW)
   sleep(0.1)
      
   GPIO.setup(resistorPin, GPIO.IN)

   kit = MotorKit()

   previous = False
   while(True):
      current = (GPIO.input(resistorPin) == GPIO.HIGH)
      sleep(0.1)
      print(current, previous)
      if current != previous:
         if current == True: # and closed.value == 1:
            kit.motor1.throttle = 1
            print("Motor forward")
            sleep(7)
            kit.motor1.throttle = 0
            # closed.value = 0
         else: #            elif current==False and closed.value == 0:
            kit.motor1.throttle = -1
            print("Motor Backward")
            sleep(6.3)
            kit.motor1.throttle = 0
            # closed.value = 1
      previous = current

if __name__=='__main__':
   lightMotor