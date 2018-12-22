import socket
import os
import threading
import csv

def main():
    host = '127.0.0.1'
    port = 5003
    s = socket.socket()
    s.bind((host,port))
    print('server started: ')
    s.listen(5)
    info = []
    f = open('/Users/Muralikrishna/Desktop/CNF/exam2/data.csv', 'r')
    csvreader = csv.reader(f, delimiter=",")
    for row in csvreader:
        info.append(row)

    while True:
        c, addr = s.accept()
        roll = c.recv(1024).decode()
        print('Connected User: ' + roll)
        threading.Thread(target = question, args = (str(roll), c, info)).start()
        #start_new_thread( question, (str(roll), c, info))
    s.close()

def question(roll,c,info):
    for row in info:
        if roll in row:
            c.send(str(row[1]).encode())
            if str(c.recv(1024).decode()) == str(row[2]):
                c.send("ATTENDANCE SUCCESS".encode())
            else:
                c.send("ATTENDANCE FAILUE".decode())
        else:
            c.send("ROLLNUMBER-NOTFOUND".encode())
            break
                
if __name__ == '__main__':
    main()
 