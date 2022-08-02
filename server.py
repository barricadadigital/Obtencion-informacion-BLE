import socket
import os

SERVER_HOST = "Introducir_IP"
SERVER_PORT = 443
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

def conexion():

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((SERVER_HOST, SERVER_PORT))

    s.listen(5)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

    client_socket, address = s.accept()
    print(f"[+] {address} is connected.")

    received = client_socket.recv(BUFFER_SIZE).decode('utf-8')
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)

    with open(filename, "wb") as f:
        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            f.write(bytes_read)
    client_socket.close()
    s.close

while True:
	conexion()
