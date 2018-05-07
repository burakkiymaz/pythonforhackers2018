import socket

soket = socket.socket()

host = '172.19.20.128'

linuxPortlar = ["22"]
windowsPortlar = ["135", "137"]

for i in range(1,81):
    try:
        soket.connect((host, i))
        veri = str(soket.recv(1024))
        if len(veri):

            print("port acik ", str(i))
            print("Banner\n")
            print(veri)
            if str(i) in linuxPortlar:
                dosya = open("Linux.txt", "a")
                dosya.write(str(host))
                dosya.close()
                print("[+] Linux bir sistem olabilir.")
            elif str(i) in windowsPortlar:
                print("[+] Windows bir sistem olabilir.")
    except:
        # print("[-] Sistem yok")
        pass