import socket, pickle, sys, time
from copy import deepcopy as dc

connected = False
im = None
im_string = None

if 'pyscreenshot' in sys.modules:
    import pyscreenshot as ImageGrab
else:
    print("Please install pyscreenshot!\npip install pyscreenshot")
    while True:
        time.sleep(60)
    exit()

def imgloop():
    while True:
        if connected: # Save Resources
            im = ImageGrab.Grab()
            im_string = pickle.dumps(im)
        else:
            time.sleep(1)

it = threading.Thread(target = imgloop)
it.start()
            
def servloop():
    tim = None
    while True:
        if tim != im_string:
            tim = dc(im_string)
            s.send(bytes(tim, "utf-8"))
            
HOST = socket.gethostname()
PORT = 61734

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

while True:
    if not connected:
        conn, addr = sock.accept()
        connected = True
    else:
        continue
    
    st = threading.Thread(target = servloop)
    st.start()
