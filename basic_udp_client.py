import socket 

t_host = "127.0.0.1"
t_port = 9856

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # standard ipv4 adress // udp client

client.sendto(b"AAABBBCCC", (t_host, t_port))

client.settimeout(5)
try:
    data, addr = client.recvfrom(4096)
    print(data.decode())
except socket.timeout:
    print("Socket timeout")

client.close()