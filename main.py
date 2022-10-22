from imp import IMP_HOOK
import imp
import RPi.GPIO as GPIO
import time
import blueT



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Right motor
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

#Left Motor
GPIO.setup(21, GPIO.OUT);
GPIO.setup(20, GPIO.OUT)

GPIO.output(5,GPIO.LOW)
GPIO.output(6, GPIO.LOW)

blueT.sendMessageTo("14:5A:FC:69:1B:1C")