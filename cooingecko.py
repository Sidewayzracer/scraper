import requests
import json
import os


t = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=algorand&vs_currencies=usd').text
t = json.loads(t)
price = float(t["algorand"]["usd"])

print(price)
