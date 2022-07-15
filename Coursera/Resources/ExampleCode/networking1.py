#this is a small implementation of a web browser that requests data from the url below.

import socket

#used for initiating a connection not preparing to receive connections
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a streamed internet socket
mysocket.connect( ('www.py4inf.com', 80) ) #use port 80 for HTTP requests, establish a connection at the website's port 80

mysocket.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n') #using HTTP 1.0 protocol. Need to send two enters or \n to finish the request.

while True:
	data = mysocket.recv(512) #receive up to 512 bits of data at a time
	if (len(data) < 1 ): #if we do not receive any data then break the connection
		break
	print data
mysocket.close() #close the socket
