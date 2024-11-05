import socket

host = ''    # host of server socket
port = 12800  # port of server socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create TCP client socket
data = ""
client_socket.connect((host, port)) # Connect to the server socket
print(f"Connected to server at {host}:{port}")

prompt = client_socket.recv(1024).decode('utf-8')
print(prompt)

user_input = input()
client_socket.sendall(user_input.encode('utf-8'))

response = client_socket.recv(1024).decode('utf-8')
print(response)

if "Granted" in response:
    print("connected")
    prompt_data_input = client_socket.recv(1024).decode('utf-8')
    print(prompt_data_input)
    while True:
        data +=input("")
        if "end" in data:
            client_socket.sendall(data.encode('utf-8'))
            break

    confirmation_msg = client_socket.recv(1024).decode('utf-8')
    print(confirmation_msg)
        

else:
    print("not connected")

