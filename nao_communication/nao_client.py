import socket

class NaoClient:
    def __init__(self, ip, port=5000):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ip, self.port))

    def send_message(self, message):
        self.sock.sendall(message.encode())

    def close(self):
        self.sock.close()
