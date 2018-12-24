# importing socket libraries
import socket
import sys
import threading
import random

def function(c, data):
    #Randomly takes the value btw 1 to 100
    gv = random.randint(1,100)
    #printing guess value
    print("Your guess is: " + str(gv))

    while True:
        #-------------------------------------------------------
        dat = int(data.strip())
        if dat > gv:
            c.send("Your number is greater than guess...".encode())
        #---------------------------------------------------------
        elif dat < gv:
            c.send("Your number is lesser than guess...".encode())
        #---------------------------------------------------------
        elif dat == gv:
            c.send(("Your Guess is Correct."+"\n"+"You are the winner.").encode())
            c.send("q".encode())
            break
        #--------------------------------------------------------
        data = c.recv(1024).decode()

# main function.
def main():
    host = '127.0.0.1'
    port = 5005

    #creating socket object
    s = socket.socket()

    #binding socket object to port and host
    #bind func takes only one argument.
    s.bind((host, port)) #11

    #listening for message from socket
    s.listen(10)

    # server connection
    print ("Server Started....")

    #Recieving data from client and executing the required function.
    while(True):

        #connection and address of client
        c, address = s.accept() #11

        #buffering data which is recieved
        data = c.recv(1024) #2

        #print the connection IP and PORT
        print("Recieved connection from: "+str(address))

        #Breaking conection if no Data
        if not data:
            break

        #thread for client
        threading.Thread(target = function, args=(c, str(data.decode()))).start()

    #print for session termination
    print("---------session terminated------------")
    print("")
    
    #closing the connection
    c.close()

if __name__ == '__main__':
    main()