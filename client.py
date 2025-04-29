#!/usr/bin/env python3
import socket

SERVER_IP   = "169.254.242.81"  # ← your NAO’s IP
SERVER_PORT = 10000

def main():
    # Create and connect the socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((SERVER_IP, SERVER_PORT))
        print(f"Connected to {SERVER_IP}:{SERVER_PORT}")

        while True:
            message = input('Enter message (or "exit"): ')
            if message.lower() == 'exit':
                print("Exiting.")
                break

            # Send (must be bytes)
            sock.sendall(message.encode('utf-8'))

            # Receive and decode
            data = sock.recv(1024)
            if not data:
                print("Server closed connection.")
                break

            print("Received:", data.decode('utf-8'))

if __name__ == "__main__":
    main()