import socket
#The socket module in Python which allows you to create,
#configure,and manage network sockets for various types of communication, including TCP and UDP.

# Define the allowed IP addresses //Implementing firewall
allowed_ips = ['127.0.0.3','127.0.0.1', '102.215.79.242']  # Add the IP addresses you want to allow

#Socket creation
# socket():  Creates a new socket object.
# You can specify the type of socket (e.g., socket.AF_INET for IPv4, socket.AF_INET6 for IPv6)
#socket type = socket.SOCK_STREAM for TCP, socket.SOCK_DGRAM for UDP.

s = socket.socket() 
print('Socket successfully created')
# Checking whether the socket has been created. 
port = 56789

# Before the loop, bind the sockets.
# 'bind()': This method is used to associate a socket with a specific network address
s.bind(('', port))
print(f'Socket bound to port {port}')
s.listen(5) #Backlog ie.The maximum number of clients thar can make a request at the same time. 
print('Socket is listening')
# Server is ready to accept requests

while True:
     #This creates an infinite loop. The server will keep running and accepting connections until it is manually stopped or an exception occurs.
    # Accept the connection once a request has been made by the client

    c, addr = s.accept()

     # The returned values from the accept method are assigned to variables "c" and "addr"
     #c is the new socket object representing the specific connection with the client
     #"addr" is the address of the client.


     #Implementing firewall.
    # Get the connecting IP and check if it is allowed
    connecting_ip = addr[0]  # Getting the Clients' IP Address.
    if connecting_ip not in allowed_ips:  #Checking whether the connecting IP Address is allowed. 
        errormessage = 'Your ip is not allowed'
        c.send(errormessage.encode()) 
        print('Connection from', connecting_ip, 'rejected. Not an allowed IP.')
        c.close()
        continue

    print('Got connection from', addr)
    message = 'Thank you for connecting'  #Successful connection.
    c.send(message.encode())
    c.close()
