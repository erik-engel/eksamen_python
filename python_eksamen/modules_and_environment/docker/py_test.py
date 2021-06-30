import requests

x = requests.get('http://worldtimeapi.org/api/timezone/Europe/Copenhagen')

print(x.text)

