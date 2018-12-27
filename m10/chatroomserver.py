import socket
import os
import threading
import time
import signal
#main function
def Main():
	host = '127.0.0.1'
	port = 5003
	s = socket.socket()
	s.bind((host,port))
	print("Server Started....")
	#can chat up to 10 users
	s.listen(10)
	#connections list
	clientlist = []
	#dictionary of id names and connections
	#where, key is connection; value is id
	connectiondictionary = {}
	#connecting with each client.
	while True:
		c, addr = s.accept()
		c.send("=========W3LC0M3 T0 CH4TR00M=========".encode())
		c.send(("\n" + "Enter your Name: ").encode())
		clientid = c.recv(1024)
		print('Connected User: ' + clientid.decode())
		connectiondictionary[c] = str(clientid.decode())
		clientlist.append(c)
		for connection in clientlist:
			if c != connection:
				connection.send((connectiondictionary[c] + ' is Connected.').encode())
		#setting thread for each client.
		threading.Thread(target = chatclients, args = (c, addr, clientlist, connectiondictionary)).start()
	#closing server
	s.close()
#-----------------------------------------------------------------
#checkclientsing number of connections
#if only one shuts after 10 sec..
def checkclients():
	print(active_count())
	if (active_count() == 2):
		print('Waiting for Connections....')
		time.sleep(10)
		if (active_count() == 2):
			os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
#-----------------------------------------------------------------
#chatroom function thread
def chatclients(c, addr, clientlist, connectiondictionary):
	while True:
		try:
			message = (c.recv(1024)).decode()
			print(connectiondictionary[c] + '<-->' + message)
			if message != 'x' and c in clientlist:
				for client in clientlist:
					if c != client:
						try:
							clientname = connectiondictionary[c]
							client.send((clientname + '-->' + message).encode())
						except:
							c.close()
							removeclient(c, clientlist)
			else:
				c.send(('Do you want to Exit?(Y/N)').encode())
				if ((c.recv(1024)).decode() == 'Y'):
					for con in clientlist:
						if c != con:
							con.send((connectiondictionary[c] + ' is disconnected. Users online: ' + str(active_count() - 2)).encode())
					c.send('Disconnect'.encode())
					removeclient(c,clientlist)
					checkclients()
					return 1
		except:
			continue
	c.close()
#------------------------------------------------------------------------------
#removing client from chatroom
def removeclient(c, clientlist):
	if c in clientlist:
		clientlist.removeclient(c)
#-----------------------------------------------------------------------------
if __name__ == '__main__':
	Main()