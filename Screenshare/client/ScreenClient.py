from tkinter import *
import threading
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = int(input("Port: "))
host = input("Hostname: ")

try:
    s.connect((host, port))
except:
    exit()

class GUI:
    def __init__(self, master, s):
        self.master = master
        master.title = "Client"
        self.s = s
        self.pic = 0

        self.strt_btn = Button(self.master, command = self.Start, text = "Start!")
        self.strt_btn.pack()

        self.buff = 0

    def Loop(self):
        Data = self.s.recv(2560000)
        Data += self.s.recv(2560000)
        if self.buff == 0:
            self.buff = 1
            print("Buffer.")
            return
        else:
            print("Got picture from host.")

        if self.pic == 0:
            self.pic = 1
        elif self.pic == 1:
            self.pic = 2
        elif self.pic == 2:
            self.pic = 0

        try:
            os.remove("Picture"+str(self.pic)+".png")
            print("Removed old picture.")
        except:
            pass

        print("Generating new picture...")
        File = open("Picture"+str(self.pic)+".png", "wb")
        File.write(Data)
        File.close()

        time.sleep(.1)

        print("Displaying new image.")
        img = PhotoImage(file = "Picture"+str(self.pic)+".png")
        self.label.configure(image = img)
        self.label.image = img
        

    def Looper(self):
        while 1:
            self.Loop()

    def Start(self):
        self.strt_btn.destroy()
        
        self.label = Label(self.master)
        self.label.pack()

        thread = threading.Thread(target = self.Looper)
        thread.start()

root = Tk()
gui = GUI(root, s)
root.mainloop()
