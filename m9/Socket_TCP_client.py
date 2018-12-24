# importing socket libraries
import socket
import sys

# main function
def main():
    host = '127.0.0.1'
    port = 5005

    #creating socket object
    s = socket.socket()

    # connecting with Server
    # connect func takes only one argument
    s.connect((host, port)) #11

    #welcoming message
    print("---------------Welcome To GuessGame----------")

    #taking input from console
    message = input("Enter your guess here --> : ")

    #Condition for terminating connection:
    while(message != 'q'):
        # sending message for server
        s.send(message.encode()) #1

        #recieving processed data from server
        data = s.recv(1024)

        #printing  the data recieved
        print(str(data.decode()))

        if(len(str(data.decode())) > 40):
            break

        #taking input from console
        message = input("Enter your guess here -->: ")

    #print for session termination
    print("---------session terminated------------")
    print("")
    
    #closing connection from client
    s.close()

if __name__ == '__main__':
    main()