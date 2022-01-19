import socket

s=socket.socket()
print("Socket Created")

remoteDetail=("127.0.0.1",1234)
s.connect(remoteDetail)

print("Connected to Server")

msg=s.recv(1024)
print("Server :",msg)
s.close()
print("Client closed")