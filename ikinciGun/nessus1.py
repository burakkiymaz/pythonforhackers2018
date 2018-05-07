import requests
header={"X-ApiKeys": "ApiKeys"} # Buraya Nessus dan alınan ApiKey yazılacak
url="https://127.0.0.1:8834/folders"
sonuc=requests.get(url=url,headers=header,verify=False)
for i in sonuc.json()['folders']:
    if "isletme" in i['name']:
        try:
            print "Yapilma tarihi:",str(i['name']).split("_")[1]
        except:
            pass
