import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Right motor
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
#Left Motor
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

GPIO.output(5, GPIO.HIGH)
GPIO.output(6, GPIO.LOW)