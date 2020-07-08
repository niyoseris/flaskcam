import requests
import time
import os

def fotoCek():
    os.system("fswebcam --save a.jpg")
    files = {'file': open('a.jpg', 'rb')}
    z = requests.post("https://***.eu/", files=files)
    print (z.content)

while True:
    sT = open("x.txt", "r")
    gf = sT.read
    sT.close()

    lastFoto = requests.get("http://***.eu/static/t.txt")

    if gf = lastFoto:
        pass
    else:
        fotoCek()
