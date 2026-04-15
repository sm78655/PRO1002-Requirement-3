import socket

host = "example.com"
ip_address = socket.gethostbyname(host)

print("Hello! The resolved IP address is:", ip_address)
