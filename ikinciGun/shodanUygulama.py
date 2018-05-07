import requests
url="shodanKey" #buraya shodan dan alınan API key girilecek...
sonuc=requests.get(url=url,verify=False)
for i in sonuc.json()['data']:
    print i
