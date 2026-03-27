from socket import *
serveName = '172.20.66.195'
servePort = 12000
clinetSocket = socket(AF_INET, SOCK_DGRAM)
message = input('input sth to make it upper\n')
clinetSocket.sendto(message.encode(), (serveName, servePort))
retMessage, serveAddr = clinetSocket.recvfrom(2048)
print(retMessage.decode())
clinetSocket.close()