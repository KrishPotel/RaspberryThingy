# echo-client.py

import socket

HOST = "192.168.68.163"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    while True:
        data = s.recv(1024)
        if data == b"W":
            print("WOOOOOOOOOOOOOOOOO")    
        print(f"Received {data!r}")