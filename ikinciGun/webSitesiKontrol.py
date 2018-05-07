import requests
import datetime
import time
# tarih|sonuc.status_code|url
url="https://www.tenable.com/downloads/nessus"
sonuc=requests.get(url,verify=False)
gercekIcerik= sonuc.content
dosya=open("icerik.txt","w")
dosya.write(gercekIcerik)
dosya.close()

while 1:
    url = "https://www.tenable.com/downloads/nessus"
    sonuc = requests.get(url, verify=False)
    icerik= sonuc.content
    print sonuc.status_code
    log=str(datetime.datetime.now())+"|"+str(sonuc.status_code)+"|"+str(url)+"\n"
    logDosya=open("loglar.txt","a")
    logDosya.write(log)
    logDosya.close()
    if str(sonuc.content) in gercekIcerik:
        print "Degisiklik yok"
    else:
        print "Site degisiklik var"
    time.sleep(60nilbarany)