# importing socket libraries
import socket
import sys
def main():
	host = '127.0.0.1'
	port = 54321

	#creating socket object
	s = socket.socket()

	#binding socket object to port and host
	#bind func takes only one argument.
	s.bind((host, port))

	#listening for message from socket
	s.listen(1)

	#connection and address of client
	c, address = s.accept()

	# print the connection IP and PORT
	print ("Recieved conection from " + str(address))

	#Recieving data from client and executing the required function.
	while(True):
		#buffering data which is recieved
		data = c.recv(1024)

		#Breaking conection if no Data
		if not data:
			break

		# Printing what data recieved
		print ("Data recieved from user: " + str(address))

		#converting data into UPPER CASE
		data = str(data.decode()).upper()

		#printing converted data
		print ("sending data: " + str(data))

		#sending data to client
		c.send(data.encode())
	#closing the connection
	c.close()

if __name__ == '__main__':
	main()