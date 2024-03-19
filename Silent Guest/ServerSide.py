import socket

# Create a socket object for the server
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Hostname or IP address of the server
host = socket.gethostname()
# Port number to listen on
port = 9999

# Bind the socket to the host and port
serversocket.bind((host, port))

# Listen for incoming connections
serversocket.listen(1)

while True:
    # Accept a connection from the client
    clientsocket, addr = serversocket.accept()
    print("Connection established with", addr)

    # Send a command to the client
    command = input("Enter command to execute on client: ")
    clientsocket.send(command.encode())

    # Receive the output from the client
    output = clientsocket.recv(4096).decode()
    print("Output from client:", output)

    # Close the connection with the client
    clientsocket.close()
