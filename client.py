import socket

host = '192.168.1.70'    # host is ip address of server machine
port = 12800  # port of server socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #create TCP client socket
data = ""
client_socket.connect((host, port)) # Connect to the server socket
print(f"Connected to server at {host}:{port}")

prompt = client_socket.recv(1024).decode('utf-8')#fetch the password prompt from server
print(prompt)

user_input = input()  #store input of password in user_input
client_socket.sendall(user_input.encode('utf-8')) #send user_input to server

response = client_socket.recv(1024).decode('utf-8')#fetch the repsonse message from server
print(response)

if "Granted" in response: #correct password connection allowed
    print("connected")
    prompt_data_input = client_socket.recv(1024).decode('utf-8')#fetch data input prompt message from server
    print(prompt_data_input)
    while True:
        data +=input("") #append data unitl 'end'
        if "end" in data:
            client_socket.sendall(data.encode('utf-8'))#send data to server
            break

    confirmation_msg = client_socket.recv(1024).decode('utf-8')#fetch confirmation message from server
    print(confirmation_msg)
        

else: #incorrect password connection not allowed
    print("not connected")

