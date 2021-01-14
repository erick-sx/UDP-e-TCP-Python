from socket import *
serverPort = 12000 #abre a porta no servidor
serverSocket = socket (AF_INET,SOCK_DGRAM) #define o protocolo do socket
serverSocket.bind(('',serverPort)) #Associa o host com a porta 
print("Servidor pronto para receber") #mensagem de aviso que o server está pronto
while True: #Como o servidor deve estar sempre aberto, criamos loop infinito
	message, clientAddress = serverSocket.recvfrom(2048) #Recebe do client a mensagem em minúsculo
	modifiedMessage = message.decode().upper() #converte a mensagem em upper
	print (clientAddress,"diz:",message.decode())
	serverSocket.sendto(modifiedMessage.encode(),clientAddress) #envia para o cliente a mensagem convertida em upper
