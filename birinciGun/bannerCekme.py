import socket

soket = socket.socket()

host = '172.19.20.128'

for port in range(1,81):
    try:
        soket.connect((host,port))
        print(soket.recv(1024))
        # print "acik"
        soket.close()
    except:
        print("port kapali")