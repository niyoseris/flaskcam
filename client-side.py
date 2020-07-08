import requests
import time
import os

def fotoCek():
    os.system("fswebcam --save a.jpg")
    files = {'file': open('a.jpg', 'rb')}
    z = requests.post("https://455.eu/", files=files)
    print (z.content)

while True:
    sT = open("x.txt", "r")
    gf = sT.read()
    sT.close()

    lastFoto = requests.get("http://455.eu/static/t.txt").content

    if gf in str(lastFoto):
        print ("same")
    else:
        print (lastFoto)
        saveTime = open("x.txt", 'w')
        saveTime.write(lastFoto)
        saveTime.close()
        fotoCek()
