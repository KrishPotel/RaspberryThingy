import blueT

def receiveMessages():
  server_sock=blueT.BluetoothSocket( blueT.RFCOMM )
  
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
  sock=blueT.BluetoothSocket( blueT.RFCOMM )
  sock.connect((targetBluetoothMacAddress, port))
  sock.send("hello!!")
  sock.close()
  
def lookUpNearbyBluetoothDevices():
  nearby_devices = blueT.discover_devices()
  for bdaddr in nearby_devices:
    print(str(blueT.lookup_name( bdaddr )) + " [" + str(bdaddr) + "]")

lookUpNearbyBluetoothDevices()  
while True:
  receiveMessages()