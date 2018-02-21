import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('www.py4inf.com', 80))
cmd='GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

while True:
    data = mysocket.recv(512)
    if ( len(data) < 1 ) :
        break
    print(data.decode(), end='')
mysocket.close()
