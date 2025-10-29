import socket

# client settings (must be the same as server's)
HOST = '127.0.0.1'
PORT = 65432

# 1. Creating socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        # 2. Connecting to server
        s.connect((HOST, PORT))
        print(f"Connected to: {HOST}:{PORT}.")

        # Receiveng welcome message
        welcome_data = s.recv(1024)
        print(f"Server: {welcome_data.decode('utf-8')}")

        # Sending message
        message = "Hello server! This is client"
        print(f"Sending: '{message}'")
        s.sendall(message.encode('utf-8'))

        # Receiving goodbye from server
        response_data = s.recv(1024)
        print(f"Server respond: {response_data.decode('utf-8')}")

    except ConnectionRefusedError:
        print("Error: Cannot connect to server. Is server running?")

print("Connection closed")