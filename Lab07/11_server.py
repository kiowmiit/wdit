import socket

HOST = '127.0.0.1'  # loopback address - 'localhost'
PORT = 65432  # Low privilege port number (> 1023)

# 1. Creating a socket
# AF_INET --> IPv4, SOCK_STREAM -> TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 2. Binding port to address and port
    s.bind((HOST, PORT))

    # 3. Start listening for connections
    s.listen()
    print(f"Listening on {HOST}:{PORT}...")

    # 4. Accepting connection from client
    # conn is a new socket, addr is client address
    conn, addr = s.accept()
    with conn:
        print(f"Connected to: {addr}")

        # Sending welcome message
        welcome_message = "Welcome client. Send your message: "
        conn.sendall(welcome_message.encode('utf-8'))
        # same as
        # conn.sendall(b"Welcome client. Send your message: ")

        # Receiving data
        data = conn.recv(1024)  # Receiveng up to 1024 bytes
        if data:
            print(f"Received from client: {data.decode('utf-8')}")

            # Sending a goodbye.
            response = "Server has received a message. Goodbye!"
            conn.sendall(response.encode('utf-8'))

    print("Connection closed.")