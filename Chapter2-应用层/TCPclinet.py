from socket import *
clientSocket = socket(AF_INET, SOCK_STREAM)
serverName = '172.20.66.195'
serverPort = 12000
clientSocket.connect((serverName, serverPort))
message = input('input sth')
clientSocket.send(message.encode())
retMessage = clientSocket.recv(1024)
print(retMessage.decode())
clientSocket.close()
