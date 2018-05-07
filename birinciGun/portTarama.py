import socket

soket = socket.socket()

host = '172.19.20.128'

for port in range(1,1024,1):
    try:
        # print str(port)
        if soket.connect_ex((host, port)) == 0:
            print(str(port) + " Numarali Port Acik")
        soket.close()
    except:
        soket.close()

