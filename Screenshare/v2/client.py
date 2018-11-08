import socket, pickle, sys, time

if 'pyscreenshot' in sys.modules:
    import pyscreenshot as ImageGrab
else:
    print("Please install pyscreenshot!\npip install pyscreenshot")
    while True:
        time.sleep(60)
    exit()

HOST = input("Host: ")
PORT = 61734
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

while True:
    im_string = str(sock.recv(1024*1024), "utf-8")
    im = pickle.loads(im_string)
    
    im.show()
