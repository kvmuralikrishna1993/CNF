# importing socket libraries
import socket
import sys

# main function
def main():
	host = '127.0.0.1'
	port = 54321

	#creating socket object
	s = socket.socket()

	# connecting with Server
	# connect func takes only one argument
	s.connect((host, port))

	#taking input from console
	message = input("Enter message here -->: ")

	#Condition for terminating connection:
	while(message != 'q'):
		# sending message for server
		s.send(message.encode())

		#recieving processed data from server
		data = s.recv(1024)

		#printing  the data recieved 
		print("Recieved data from Server: " + str(data.decode()))
		print("")

		#taking input from console
		message = input("Enter message here -->: ")

	#print for session termination
	print("---------session terminated------------")
	print("")
	
	#closing connection from client
	s.close()

if __name__ == '__main__':
	main()