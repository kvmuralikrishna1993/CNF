# importing socket libraries.
import socket
import sys
import time

def main(): 
	host = '127.0.0.1'
	port = 54321

	#creating socket object.
	#DEFAUT is socket(socket.AF_INET, socket.STREAM) == socket().
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	#binding socket object to port and host.
	#bind func takes only one argument.
	s.bind((host, port))

	# Listening started.
	print ("Ready to listen ")

	#Recieving data from client and executing the required function.
	while(1):
		data = None

		#buffering data which is recieved
		data, address = s.recvfrom(1024)

		#termination condition
		if str(data.decode()) == "stop":
			break

		# Printing adrress recieved from.
		print ("Data recieved from user: " + str(address))

		#printing recieved data.
		print ("recieved data: " + str(data.decode()))

		#converting data into UPPER CASE
		data = str(data.decode()).upper()

		#printing converted data.
		print ("sending data: " + str(data))

		#sending data to client.
		s.sendto(data.encode(), address)
		
	print("---------session terminated------------")
	#closing the connection.
	s.close()

if __name__ == '__main__':
	main()