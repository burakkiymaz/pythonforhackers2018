import requests
header={"X-ApiKeys": "accessKey=f53762e0249be564847adf5112399ed58329de16707add4b210fe18683946cac; secretKey=847aa316818162ba9b920814e137ea730e4cd7d878b0456cf01537502a4314fd;"}
url="https://127.0.0.1:8834/folders"
sonuc=requests.get(url=url,headers=header,verify=False)
for i in sonuc.json()['folders']:
    if "isletme" in i['name']:
        try:
            print "Yapilma tarihi:",str(i['name']).split("_")[1]
        except:
            pass