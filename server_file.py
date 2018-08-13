import socket
import os
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host ='192.168.43.42'
port = 12345
server_socket.bind((host,port))
print("Server socket sucessfully Created on IP : {} at port {} ".format(host,port))
server_socket.listen()
print("Server is waiting for clients to connect .... \n\n")
client_socket,client_addr = server_socket.accept()
print("Client is connected")
print("Client's IP {}:{}\n\n".format(*client_addr))
d=input("enter the path of the file")
e=input("enter the file name with extension")
z=os.path.join(d,e)
f=open(z,'rb')
name=f.name
print()
client_socket.send((name.encode()))
for line in f:    
    client_socket.send(line)
else :
    client_socket.send("EOF".encode()) 
    client_socket.close()
    server_socket.close()
