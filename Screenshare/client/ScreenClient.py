from tkinter import *
import threading
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = int(input("Port: "))
host = input("Hostname: ")

print("Created socket.")

try:
    s.connect((host, port))
except:
    exit()

print("Connected to host.")
    
class GUI:
    def __init__(self, master, s):
        print("Loading UI")
        self.master = master
        master.title = "Client"
        self.s = s
        self.pic = 0

        self.strt_btn = Button(self.master, command = self.Start, text = "Start!")
        self.strt_btn.pack()

        self.buff = 0

    def Remove(self, path):
        try:
            os.remove(path)
            print("Removed file: "+path)
        except:
            print("Could not remove file: "+path)
    
    def NextPic(p):
        if p == 0:
            return 1
        elif p == 1:
            return 2
        elif p == 2:
            return 0

    def Loop(self):
        remThread = threading.Thread(target = self.Remove, args = ("Picture"+str(self.NextPic(self.pic))+".png"))
        remThread.start()
        
        self.Remove("Picture"+str(self.pic)+".png")
        
        print("Waiting for host...")
        Data = self.s.recv(2560000)
        if self.buff == 0:
            self.buff = 1
            print("Buffer.")
            return
        else:
            print("Got data from host.")

        self.pic = self.NextPic(self.pic)

        print("Generating new picture...")
        File = open("Picture"+str(self.pic)+".png", "wb")
        File.write(Data)
        File.close()

        print("Displaying new image...")
        try:
            img = PhotoImage(file = "Picture"+str(self.pic)+".png")
            self.label.configure(image = img)
            self.label.image = img
        except:
            print("Could not display new image!")
        

    def Looper(self):
        while 1:
            self.Loop()

    def Start(self):
        self.strt_btn.destroy()
        
        self.label = Label(self.master)
        self.label.pack()

        thread = threading.Thread(target = self.Looper)
        thread.start()
        
        print("Start!")
        
root = Tk()
root.attributes("-fullscreen", True)
gui = GUI(root, s)
root.mainloop()
