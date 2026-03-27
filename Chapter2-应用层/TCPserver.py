from socket import *
welcomeSocket = socket(AF_INET, SOCK_STREAM)
welcomePort = 12000
welcomeSocket.bind(('', welcomePort))
welcomeSocket.listen(1)
print("ready to receive")
while True:
    connectionSocket, addr = welcomeSocket.accept()
    message = connectionSocket.recv(1024).decode()
    retMessage = message.upper()
    connectionSocket.send(retMessage.encode())
    connectionSocket.close()