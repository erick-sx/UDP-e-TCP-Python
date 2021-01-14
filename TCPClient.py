from socket import *
serverName = "10.230.234.69" #identifica o ip do servidor
serverPort = 12000 #identifica a porta
clientSocket = socket(AF_INET, SOCK_STREAM) #cria socket
clientSocket.connect((serverName,serverPort))
while True:
	sentence = input ('Escreva: ') #entrada do teclado
	clientSocket.send(sentence.encode()) #envia o socket criado a frase
	modifiedSentence = clientSocket.recv(64) #retorno do servidor
	print ('Do servidor: ', modifiedSentence.decode()) #mostra na tela a frase de resposta do server
clientSocket.close() #termina a conexão