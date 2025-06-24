import discord
import asyncio
import random

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith("@bot start selection"):
        # Add reaction options to the message
        await message.add_reaction("🇦")
        await message.add_reaction("🇧")
        await message.add_reaction("🇨")

        # Wait for two minutes
        await asyncio.sleep(120)

        # Select a random option
        options = ["🇦", "🇧", "🇨"]
        selection = random.choice(options)

        # Send a message announcing the selected option
        await message.channel.send(f"Option {selection} has been selected!")

client.run("MTA1NDkzMzQzMzUwMTA5Mzg4OQ.G9tOtI.U332GIOsSHxL5gX6w-Uiu8Z-AerdPYiqCzTVlw")