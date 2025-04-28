import socket
import sys
import time

def run_nao_server():
    HOST = '0.0.0.0'
    PORT = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)

    print('NAO Server Listening...')
    conn, addr = s.accept()
    print(f'Connected by {addr}')

    while True:
        data = conn.recv(1024)
        if not data:
            break
        command = data.decode()
        print(f"Executing command: {command}")
        # Here you would have NAO say the text
        # Replace below with your robot speaking API
        print(f"NAO says: {command}")

    conn.close()

if __name__ == "__main__":
    run_nao_server()
