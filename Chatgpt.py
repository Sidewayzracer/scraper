from discord.ext import commands
from crypto_names import name_map
from responses import *


import discord
import requests
import json

TOKEN = "MTA1NTI1NDA2NjQ2NjM5ODI2OQ.GFKv7C.A3xVpkvHHM4QRzz2j-VrSsxKiqr4wc88g0lbMs"
CHANNEL = 988541444383997980

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())



@bot.command()
async def price(ctx, *, currency: str, days: int= 30):
    price = get_price(currency)
    if days not in (1, 7):
        days = 30
    file = discord.File(f"charts/{api_currency}_prices_30days.png")
    # add a dollar sign and round to 5 decimal places, remove trailing zeros and dots
    price_str = f"${price:.5f}".rstrip("0").rstrip(".")
    await ctx.send(file=file)
    await ctx.send(f"The current price of {currency} is {price_str}")

def get_price(currency):
    # Normalize the currency name using the name map
    global api_currency
    api_currency = name_map.get(currency.lower(), currency)
    day30graph(api_currency)
    day7graph(api_currency)
    day1graph(api_currency)
    api_url = f"https://api.coingecko.com/api/v3/simple/price?ids={api_currency}&vs_currencies=usd"
    api_response = requests.get(api_url).text
    api_response = json.loads(api_response)
    global price
    price = api_response[api_currency]["usd"]
    return price




bot.run(TOKEN)