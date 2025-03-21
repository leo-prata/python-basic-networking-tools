import socket
import threading

IP = "0.0.0.0"
PORT = 9997

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((IP, PORT))

print(f"[*] UDP server listening on {IP}:{PORT}")

while True:
    data, addr = server.recvfrom(1024)
    print(f"[*] Received from {addr}: {data.decode("utf-8")}")

    server.sendto(b"received")