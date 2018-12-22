import socket
import os,signal

def main():
    host = '127.0.0.1'
    port = 5003
    s = socket.socket()
    s.connect((host,port))
    print("MARK-ATTENDANCE CHECK")
    print("------------------------------------")
    message = input("Enter your ROll NO: ")
    while message != "q":
        s.send(message.encode())
        data = s.recv(1024).decode()
        message = input(str(data) + ": ")
        data = s.recv(1024).decode()
        print(str(data))
        if str(data) == "ATTENDANCE SUCCESS":
            break
        message = input("Enter your ROll NO: ")
    s.close()
if __name__ == '__main__':
    main()