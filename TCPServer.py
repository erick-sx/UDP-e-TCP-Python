from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM) #cria socket
serverSocket.bind(("10.230.234.69", serverPort)) #associa a porta ao socket
serverSocket.listen(1) #numero de conexões disponíveis a realizar
print ("O servidor está pronto para receber")
connectionSocket, adr = serverSocket.accept() #aceita conexão e recebe a mensagem
while  True:
	sentence = connectionSocket.recv(64).decode()
	#capitalizedSentence = sentence.upper()
	#connectionSocket.send(capitalizedSentende.encode())
	print(sentence)
	a = input(": ")
	connectionSocket.send(a.encode())
connectionSocket.close()
