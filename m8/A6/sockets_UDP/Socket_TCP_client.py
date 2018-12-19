# importing socket libraries
import socket
import sys

# main function
def main():

	# ^^^^^indirectly setting up a Server^^^^^^^

	host = '127.0.0.1'
	port = 54322

	#desination server
	server = ('127.0.0.1', 54321)

	#creating socket object for UDP
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# bind func takes only one argument
	s.bind((host, port))

	#taking input from console
	message = input("Enter message here -->: ")

	#Condition for terminating connection:
	while(message != 'q'):

		# sending message for server
		s.sendto(message.encode(), server)

		#recieving processed data from server
		data, address = s.recvfrom(1024)

		#printing  the data recieved 
		print("Recieved data from Server: " + str(data.decode()))

		#taking input from console
		message = input("Enter message here -->: ")

	#termination for server
	terminate = "stop"
	s.sendto(terminate.encode(), server)

	#print for session termination
	print("---------session terminated------------")
	
	#closing connection from client
	s.close()

if __name__ == '__main__':
	main()