import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sonuc = client.connect("159.65.201.54", username="root", password="test1234")
a, b, c = client.exec_command("pwd")
print(a)
print(b)
print(c)
client.close()
