# importing socket libraries
import socket
import sys

def value(string):
	#Spliting Data.
	data = string.split(" ")

	if (data[4] == "Dollar"):
	#required in dollars.
		if(data[1] == "Yen"):
			return int(data[2])/113.41 
		elif(data[1] == "INR"):
			return int(data[2])/67
		elif(data[1] == "Pounds"):
			return int(data[2])/0.75

	elif(data[4] == "Yen"):
	#required in Yens.
		if(data[1] == "Dollar"):
			return int(data[2])*113.41 
		elif(data[1] == "INR"):
			return (int(data[2])/67)*113.41
		elif(data[1] == "Pounds"):
			return (int(data[2])/0.75)*113.41

	elif(data[4] == "INR"):
	#required in INR.
		if(data[1] == "Dollar"):
			return int(data[2])*67 
		elif(data[1] == "Yen"):
			return (int(data[2])/113.41)*67
		elif(data[1] == "Pounds"):
			return (int(data[2])/0.75)*67

	elif(data[4] == "Pounds"):
	#required in Pounds.
		if(data[1] == "Dollar"):
			return int(data[2])*0.75 
		elif(data[1] == "Yen"):
			return (int(data[2])/113.41)*0.75
		elif(data[1] == "INR"):
			return (int(data[2])/67)*.75

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
		data = value(str(data.decode()))

		#printing converted data
		print ("sending data: " + str(data))

		#sending data to client
		c.send(str(data).encode())

	#print for session termination
	print("---------session terminated------------")
	print("")
	
	#closing the connection
	c.close()

if __name__ == '__main__':
	main()