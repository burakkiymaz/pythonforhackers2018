import requests
url="https://api.shodan.io/shodan/host/172.217.169.142?key=SLs2hD4d6Si43BPpEclUdsmDbA6ZNV70"
sonuc=requests.get(url=url,verify=False)
for i in sonuc.json()['data']:
    print i