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



def display_box_grid(rows, columns):
    def display_box_grid(rows, columns, emoji1, emoji2):
        grid = ""
        for row in range(rows):
            for column in range(columns):
                if row == 0 or row == rows - 1:
                    # Add a border to the top or bottom row
                    grid += "+---"
                else:
                    # Add spaces to the other rows
                    grid += "|   "
            grid += "+\n"
            for column in range(columns):
                if row == 0 or row == rows - 1:
                    # Add a border to the top or bottom row
                    grid += "   "
                else:
                    # Choose a random emoji for this cell
                    if random.randint(0, 1) == 0:
                        grid += f"| {emoji1} "
                    else:
                        grid += f"| {emoji2} "
            grid += "|\n"
        for column in range(columns):
            grid += "+---"
        grid += "+\n"
        return grid

@bot.command()
async def grid(ctx):
    if ctx.message.content.startswith('!grid'):
        rows, columns = map(int, ctx.message.content[6:].split())
        grid = display_box_grid(rows, columns)
        await ctx.send(grid)

bot.run(TOKEN)