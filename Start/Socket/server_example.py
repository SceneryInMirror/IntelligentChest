import socket
import threading
import time

# Init
# server ip: 162.105.91.29
# server port: 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('162.105.91.29',9999))
s.listen(5)
print ('waiting for connection...')

# handle cmd
def upload():
    pass
def remove():
    pass
def keywordsearch():
    pass
def detailsearch():
    pass
def identify():
    pass
def error():
    print ('error')
# distribute cmd to different functions
def cmd_distribute(cmd):
    distribute = {
        'upload': upload(),
        'remove': remove(),
        'keywordsearch': keywordsearch(),
        'detailsearch': detailsearch(),
        'identify': identify(),
    }
    return distribute.get(cmd, error())

# response to the client
def tcplink (sock, addr):
    print ('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    data = sock.recv(1024)
    cmd = data.decode('utf-8')
    cmd_distribute(cmd)
    sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))

    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print ('Connection from %s:%s closed.' % addr)


# every connect will get an isolated thread
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock,addr))
    t.start()
