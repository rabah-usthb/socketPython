import socket 

host = ''         #default host 
data = ""
port = 12800                                                #using free port 5000
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)           #setup TCP socket 
server_socket.bind((host,port))                            #Bind the socket to the host and port
server_socket.listen()  # The server starts listening for client connections
print(f"server socket start listening at host {host} port {port}")

while True:
    client_socket , client_address = server_socket.accept() #waiting for client connection
    print(f"Client {client_address} is trying to connect")

    password_prompt = ("Input Server Password : ") #prompt client to input password
    client_socket.sendall(password_prompt.encode('utf-8'))

    user_input_code = client_socket.recv(1024).decode('utf-8')
    

    if user_input_code == '1234':
        print(f"Correct password connection to {client_address} successfull")
        client_socket.sendall("Acess Granted".encode('utf-8'))
        #if client logged in correctly start receiving message until keyword end
       
        client_socket.sendall("Input Data (To quit type 'end')".encode('utf-8'))
        while True:
            data = client_socket.recv(1024).decode('utf-8')  # Receive data from the client
            if data == "":
                print(f"Connection with {client_address} has been closed, message not received")
                break
            elif "end" in data: 
                print(f"message received {data}")
                client_socket.sendall("Messaged was received successfully".encode('utf-8'))
                break

        client_socket.close()
    else:
        print(f"Error Incorrect Password connection denied to {client_address}")
        client_socket.sendall("Acess Denied".encode('utf-8'))
        client_socket.close()

