import requests
print("nhập địa điểm")
answ = input()
url = "https://api.openweathermap.org/data/2.5/weather?q=" +answ+ "&appid=53c361690f181bb571cb47a71dd2e5cd"
resu = requests.get(url)
print(resu.json())