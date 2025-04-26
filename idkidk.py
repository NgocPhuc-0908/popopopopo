import requests
imurl = "https://manhteky123-banking.hf.space/currentCK"
resu = requests.get(imurl)
print(resu.json())