import socket

t_host = "www.google.com"
t_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # standard ipv4 adress // tcp client

client.connect((t_host, t_port))

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n") # data as bytes

response = client.recv(4096) # max amount of data to be received

print(response)
client.close()