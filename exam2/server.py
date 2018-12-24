import socket
import os
import threading
import csv

'''check the connections using numbers
        on client and server side of program.'''

def main():
    host = '127.0.0.1'
    port = 5005
    s = socket.socket()
    s.bind((host,port))
    print('server started: ')
    s.listen(5)
    info = []
    #path assigned depending on my folder path
    #reading the csv file
    f = open('/Users/Muralikrishna/Desktop/CNF/exam2/data.csv', 'r')
    csvreader = csv.reader(f, delimiter=",")
    for row in csvreader:
        info.append(row)
    f.close()
    #connecting client and server
    #creating new thread for client
    while True:
        c, addr = s.accept()
        roll = c.recv(1024).decode() #2
        print('Connected User: ' + roll)
        threading.Thread(target = attendance, args = (str(roll), c, info)).start()
    s.close()

#attendance function used by thread.
def attendance(roll,c,info):
    flag = 1
    for row in info:
        flag = flag + 1
        if roll in row:
            c.send(str(row[1]).encode()) #3
            if str(c.recv(1024).decode()) == str(row[2]): #6
                c.send("ATTENDANCE SUCCESS".encode()) #7
            else:
                c.send("ATTENDANCE FAILUE".decode()) #7
    if (flag > len(info)):
        c.send("ROLLNUMBER-NOTFOUND".encode()) #--> 3! <----
                
if __name__ == '__main__':
    main()