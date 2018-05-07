import requests
import vulndb
sozluk={"172.19.20.128":"172.217.169.142"}
header={"X-ApiKeys": "accessKey=6945e0aff46195ea7b249622842bf4c94be121eba140dda8e1c2b6457f1c1555; secretKey=7dc3a4e6ccd0e33ed76affad113f27f32c3accc72993fb3336a274be47d55858;"}
url="https://127.0.0.1:8834/scans"
sonuc=requests.get(url=url,headers=header,verify=False)
for i in sonuc.json()['scans']:
    print i['uuid'],"-",i['id']
    url = "https://127.0.0.1:8834/scans/"+str(i['id'])
    sonuc = requests.get(url=url, headers=header, verify=False)
    print sonuc.json()
    print "zafiyetler"
    for i in sonuc.json()['vulnerabilities']:
        print i['plugin_name']
        print i
    print "===="
    for i in sonuc.json()['vulnerabilities']:
        pluginName = i['plugin_name']
        IPler = sonuc.json()['info']['targets']
        if "SQL" in pluginName:
            from vulndb import DBVuln

            veritabaniID = DBVuln.from_id(42)
            rapor = "Tanim:" + str(veritabaniID.title) + "\n"
            rapor += "IP:" + str(IPler) + "\n"
            rapor += "Aciklama" + str(veritabaniID.description) + "\n"
            dosya = open("rapor.txt", "a")
            dosya.write(rapor)
            dosya.close()
    try:
        print "Taranan IPler:",sonuc.json()['info']['targets']
        publicIP=sozluk[str(sonuc.json()['info']['targets'])]
        url = "https://api.shodan.io/shodan/host/"+str(publicIP)+"?key=SLs2hD4d6Si43BPpEclUdsmDbA6ZNV70"
        sonuc = requests.get(url=url, verify=False)


    except:
        pass