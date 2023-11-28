import socket

s = socket.socket()
port = 56789
 #This sets the port number to 56789, which is the port the client will try to connect to on the server.

s.connect(('127.0.0.1', port))  #Client trying to connect to the server.
 #This initiates a connection to the server at the IP address 127.0.0.1 (localhost) and the specified port (56789).

print(s.recv(1024))
 #This line receives data from the server using the recv method.
 
s.close()
