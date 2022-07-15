#Author: Randal Obringer
#Date Last Modified: 26 September 2016
#Description: Make an http request to data.pr4e.org and pull a page from the url below.
#	Display the headers as well as the data.
#Course: Coursera via Michigan University - Using Python to Access Web Data
import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a streamed internet socket
mysocket.connect( ('data.pr4e.org', 80) ) #establish a connection at the website's port 80 used for HTTP requests

mysocket.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n') #using HTTP 1.0 protocol. Need to send two "enters or \n" to finish the request.

data = "Initialized" #ensure we run the loop once
while len(data) > 1: #if we don't receive any 
	data = mysocket.recv(512) #receive up to 512 bits of data at a time
	if (len(data) > 1):
		print data
mysocket.close() #close the socket
