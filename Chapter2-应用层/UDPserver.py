from socket import *
servePort = 12000
serveSocket = socket(AF_INET, SOCK_DGRAM)
serveSocket.bind(('', servePort))
print("serve is ready to receive")
while True:
    message, clientAddr = serveSocket.recvfrom(2048)
    retMessage = message.decode().upper()
    serveSocket.sendto(retMessage.encode(), clientAddr)
    print("finished_raw_message : " + message.decode() + "\n")
    