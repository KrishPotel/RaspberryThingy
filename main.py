# import RPi.GPIO as GPIO
# import time

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)

# #Right motor
# GPIO.setup(5, GPIO.OUT)
# GPIO.setup(6,GPIO.OUT)

# #Left Motor
# GPIO.setup(21, GPIO.OUT);
# GPIO.setup(20, GPIO.OUT)

# GPIO.output(5,GPIO.LOW)
# GPIO.output(6, GPIO.LOW)

import bluetooth

def receiveMessages():
  server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  
  port = 1
  server_sock.bind(("",port))
  server_sock.listen(1)
  
  client_sock,address = server_sock.accept()
  print("Accepted connection from " + str(address))
  
  data = client_sock.recv(1024)
  print("received [%s]" % data)
  
  client_sock.close()
  server_sock.close()
  
def sendMessageTo(targetBluetoothMacAddress):
  port = 1
  sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  sock.connect((targetBluetoothMacAddress, port))
  sock.send("hello!!")
  sock.close()
  
def lookUpNearbyBluetoothDevices():
  nearby_devices = bluetooth.discover_devices()
  for bdaddr in nearby_devices:
    print(str(bluetooth.lookup_name( bdaddr )) + " [" + str(bdaddr) + "]")
    
    
lookUpNearbyBluetoothDevices()