# echo-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
key = ""
import pygame
 
# importing sys module
import sys
 
# initialising pygame
pygame.init()
 
# creating display
display = pygame.display.set_mode((300, 300))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(), 8000))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            # creating a running loop
            while True:
                
                # creating a loop to check events that
                # are occurring
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    # checking if keydown event happened or not
                    if event.type == pygame.KEYDOWN:
                        
                        # checking if key "A" was pressed
                        if event.key == pygame.K_a:
                            key = "A"
                            print("Key A has been pressed")
                            conn.sendall(b"A")

                        # checking if key "J" was pressed
                        if event.key == pygame.K_d:
                            key = "D"
                            print("Key D has been pressed")
                            conn.sendall(b"D")

                        # checking if key "P" was pressed
                        if event.key == pygame.K_s:
                            key = "S"
                            print("Key S has been pressed")
                            conn.sendall(b"S")

                        # checking if key "M" was pressed
                        if event.key == pygame.K_w:
                            print("Key W has been pressed")
                            conn.sendall(b"W")




        