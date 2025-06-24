from discord.ext import commands
import discord
import requests
import json

TOKEN = "MTA1NTI1NDA2NjQ2NjM5ODI2OQ.GFKv7C.A3xVpkvHHM4QRzz2j-VrSsxKiqr4wc88g0lbMs"
CHANNEL = 988541444383997980


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('The bot is running')
    channel = bot.get_channel(CHANNEL)
    await channel.send('Hello Im a bot')

@bot.command()
async def hello(ctx):
    await ctx.send("hello you son of a bitch")

@bot.command()
async def price(ctx):

    t = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=algorand&vs_currencies=usd').text
    t = json.loads(t)
    price = str(t["algorand"]["usd"])
    await ctx.send('The price of Algo is ' + price)


bot.run(TOKEN)