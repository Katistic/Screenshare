import socket
import threading
import screen
import time
import os

sockets = []
output = []

host = socket.gethostname()
port = 4231

def Loop():
    while 1:
        screen.Get()
        #time.sleep(.1)
        File = open("screenshot.png", "rb")
        Data = File.read()
        File.close()
        os.remove("screenshot.png")
        
        for x in sockets:
            try:
                x.send(Data)
            except:
                sockets.remove(x)
                pprint("A client disconnected.")


def cls():
    print("\n"*150)

def pprint(t):
    cls()
    output.append(t)

    for x in output:
        print(x)

    print("Host: "+host)
    print("Port: "+str(port))

pprint("Starting Send Loop...")
thread = threading.Thread(target = Loop)
thread.start()

pprint("Creating server...")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
cls()
pprint("Server created.")
s.listen(5)

while 1:
    cs, addr = s.accept()
    sockets.append(cs)
    pprint("New connection: "+str(addr))
