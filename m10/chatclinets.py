import socket
import threading
import os,signal
#main
def Main():
    host = '127.0.0.1'
    port = 5003
    s = socket.socket()
    try:
        s.connect((host, port))
    except OSError as e:
        print("Sorry, you are Late..")
        return
    #thread for client
    thread2 = threading.Thread(target = send, args = (s,)).start()
    #disconnecting from chatroom
    while True:
        data = s.recv(1024).decode()
        if (data == 'Disconnect'):
            os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
            break
        print(data)
    s.close()
#function to send to clients..
def send(s):
    while True:
        msg = input()
        # print('MSG Sening')
        s.send(msg.encode())
    s.close()
    

if __name__ == '__main__':
    Main()
