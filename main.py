
from ast import If
from operator import truediv
from re import T
from xmlrpc.client import TRANSPORT_ERROR
import RPi.GPIO as GPIO
import time
import socket

t = False
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Right motor
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
#Left Motor
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

HOST = "192.168.68.163"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:

            if t == True:
                GPIO.output(5, GPIO.HIGH)
                GPIO.output(6, GPIO.LOW)
                GPIO.output(20, GPIO.HIGH)
                GPIO.output(21, GPIO.LOW)
            # else:
            #     GPIO.output(5, GPIO.LOW)
            #     GPIO.output(6, GPIO.LOW)
            data = conn.recv(1024)
            if data == b"W":
                print("W")
                t = True
                GPIO.output(5, GPIO.HIGH)
                GPIO.output(6, GPIO.LOW)
            elif data == b"D":
                print("D")
            elif data == b"S":
                print("S")
            elif data == b"A":
                print("A")
            elif data == b"stop":
                t = False
                GPIO.output(5, GPIO.LOW)
                GPIO.output(6, GPIO.LOW)






# GPIO.output(5,GPIO.LOW)
# GPIO.output(6, GPIO.LOW)