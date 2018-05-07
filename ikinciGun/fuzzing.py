import requests
dosya=open("fuzzingListe.txt","r")
icerik=dosya.read()
dosya.close()
print icerik
for i in str(icerik).split("\n"):
    url="http://172.19.20.128/"+str(i)
    sonuc=requests.get(url)
    if int(sonuc.status_code)==200:
        print "[+]Bulunan dosya:",str(i)