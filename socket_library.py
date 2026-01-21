import socket #importing socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating socket AF_INET is IPV4 address family, SOCK_STREAM is TCP
mysock.connect(('data.pr4e.org', 80)) #calling socket to connect to host on port 80 HTTP
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() # defining command or input to get the file and encoding to bytes
mysock.send(cmd) # sending command using .send with socket
while True: # while loop to iterate all the received data
    data = mysock.recv(1024) # using .recv with 1024 bytes to receive at once
    if (len(data)) < 1: #condition
        break
    print(data.decode()) # .decode will print the decode type, .decode() will print the ecoded data
mysock.close() # close the socket as the resources of client & server will be allocated