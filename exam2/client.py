import socket
import os,signal

'''check the connections using numbers
        on client and server side of program.'''

def main():
    host = '127.0.0.1'
    port = 5005
    s = socket.socket()
    s.connect((host,port))
    print("MARK-ATTENDANCE CHECK")
    print("------------------------------------")
    message = input("Enter your ROll NO: ")
    while message != "q":
        s.send(str(message).encode()) #1
        # if recieved is --> 3! <-- then connection will break
        data = s.recv(1024).decode() #4
        if str(data) == "ROLLNUMBER-NOTFOUND":
            print(data)
            break
        message = input(str(data) + ": ") 
        # sending answers for questions
        s.send(str(message).encode()) #5
        #recieving verification
        data = s.recv(1024).decode() #8
        print(str(data))
        break
    s.close()
if __name__ == '__main__':
    main()