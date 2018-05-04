import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('162.105.91.29',9999))

print s.recv(1024)

# s.send('GET / HTTPS/1.1\r\nHost: sceneryinmirror.github.io\r\nConnection: close\r\n\r\n')
for data in ['Michael', 'Tracy', 'Sarah']:
    s.send(data)
    print s.recv(1024)
s.send('exit')
s.close()

# header,html = data.split('\r\n\r\n', 1)

# print header
# with open('baidu.html','wb') as f:
#    f.write(html)
