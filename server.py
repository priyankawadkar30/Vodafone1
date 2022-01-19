import socket

s=socket.socket()
print("Socket Created")
remoteDetail=("",1234)
s.bind(remoteDetail)
print("Socket Binded on Port 1234")

s.listen(5)
print("Socket Server Listening")

while True:
    c,addr=s.accept()
    print("Got Connect From ",addr)

    c.send("Thanks for Joining...")

    c.close()
    print("Client Connection Closed")
    

