from socket import *

serverName = '10.230.234.60' #define o ip do servidor
serverPort = 12000	#define a porta
clientSocket = socket(AF_INET,SOCK_DGRAM) #cria o socket e o tipo do socket
while True: #client rodando pra sempre, se tirar é um socket abrindo e rodando outra vez para iniciar outra conexão
	message = input('Insere texto minusculo: ') #mensagem recebe o input do teclado
	clientSocket.sendto(message.encode(),(serverName, 12000)) #envia a mensagem para o servidor
	modifiedMessage, serverAddress = clientSocket.recvfrom(20448) #recebe a mensagem do servidor
	print (modifiedMessage.decode()) #mostra a mensagem recebida do servidor
clientSocket.close() #termina a conexão com o socket
