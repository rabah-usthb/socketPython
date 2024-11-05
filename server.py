import socket 

host = ''                                                  #default host 
port = 5000                                                #using free port 5000
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)           #setup TCP socket 
server_socket.bind((host,port))                            #Bind the socket to the host and port
server_socket.listen()  # The server starts listening for client connections
print(f"server socket start listening at host {host} port {port}")

while True:
    client_socket , client_address = server_socket.accept() #waiting for client connection
    print(f"Client {client_address} is trying to connect")

    user_input_code = input("Server Password : ") #prompt client to input password

    if user_input_code == '1234':
        print(f"Correct password connection to {client_address} successfull")
        #if client logged in correctly start receiving message until keyword end
        while True:
            data = client_socket.recv(1024)  # Receive data from the client
            if not data:
                print(f"Connection with {client_address} has been closed.")
                break
            elif " end" in data.decode('utf-8'): 
                print(f"message ended")
                break

        client_socket.close()
    else:
        print(f"Error Incorrect Password connection denied to {client_address}")
        client_socket.close()

