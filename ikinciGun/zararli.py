import requests
import subprocess
#172.19.20.1.59408

blacklist=[]
url="https://lists.blocklist.de/lists/ssh.txt"
sonuc=requests.get(url,verify=False)
for i in sonuc:
    try:
        print i
        blacklist.append(str(i))

    except:
        pass
blacklist.append("172.19.20.128")
while 1:
    try:
        paket=subprocess.check_output("tcpdump -i vmnet2 -c 1",shell=True)
        print paket
        if "IP" in paket:
            src=str(paket).split(" ")[2].split(".")[0]+"."+str(paket).split(" ")[2].split(".")[1]+"."+str(paket).split(" ")[2].split(".")[2]+"."+str(paket).split(" ")[2].split(".")[3]
            dst=str(paket).split(" ")[4].split(".")[0]+"."+str(paket).split(" ")[4].split(".")[1]+"."+str(paket).split(" ")[4].split(".")[2]+"."+str(paket).split(" ")[4].split(".")[3]
            #print "Dst:", str(paket).split(" ")[4].find(".",-1)
            if src in blacklist or dst in blacklist:
                print "Zararli siteye gittiniz...."
    except:
        pass