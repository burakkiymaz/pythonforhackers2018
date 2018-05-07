dosya=open("loglar.txt","r")
Icerik=dosya.read()
dosya.close()
for indis in str(Icerik).split("\n"):
    if "4" in str(indis.split("|")[1]) :
        print "Hata zamani: ",indis.split("|")[0]
