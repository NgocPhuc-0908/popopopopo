import requests
import time
from gtts import gTTS
import os
from playsound import playsound
imurl = "https://manhteky123-banking.hf.space/currentCK"
DLCK = requests.get(imurl)
SLCK = DLCK.json()['currentCK']
print(SLCK)

while True:
    imurl = "https://manhteky123-banking.hf.space/currentCK"
    DLCK = requests.get(imurl)
    if SLCK == DLCK.json()['currentCK']:
        time.sleep(2)
    else:
        imurl = "https://manhteky123-banking.hf.space/lastCK"
        DLCK = requests.get(imurl)
        print(DLCK.json())
        red = "bạn đã nhận được" + str(DLCK.json()['transferAmount']) + "đồng"
        tts = gTTS(text=red, lang='vi')
        tts.save("mone.mp3")
        playsound("mone.mp3")
        SLCK += 1