import socket
import threading
import screen
import os

sockets = []

def Loop():
    screen.Get()
    File = open("screenshot.png", "rb")
    Data = File.read()
    File.close()
    os.remove("screenshot.png")
    
    for x in sockets():
        x.send(Data)

def cls():
    print("\n"*150)

print("Starting Send Loop...")
thread = threading.Thread(target = Loop())
thread.start()

print("Creating server...")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 4231
s.bind((host, port))
cls()
print("Server created.")
print("Host: "+host)
print("Port: "+port)
s.listen(5)

while 1:
    cs, addr = s.accept()
    sockets.append(cs)
