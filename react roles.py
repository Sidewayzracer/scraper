import discord
from discord.ext import commands

TOKEN = 'MTA1NTI1NDA2NjQ2NjM5ODI2OQ.GFKv7C.A3xVpkvHHM4QRzz2j-VrSsxKiqr4wc88g0lbMs'
CHANNEL = 1061011855797137428

# Create an Intents object with the required events
intents = discord.Intents().all()

# Pass the intents to the Client constructor
client = discord.Client(intents=intents)

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

emoji_roles = {
    "🧠": "Finance Ape",
    "🥊": "Rumbler",
    "🍆": "Poker Ape",
}


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

# Add roles
@client.event
async def on_raw_reaction_add(payload):
    guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)
    role_name = emoji_roles.get(payload.emoji.name)

    if role_name and payload.message_id == 1061040263356760205:
        role = discord.utils.get(guild.roles, name=role_name)
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)

# Remove roles
@client.event
async def on_raw_reaction_remove(payload):
    guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)
    role_name = emoji_roles.get(payload.emoji.name)

    if role_name and payload.message_id == 1061040263356760205:
        role = discord.utils.get(guild.roles, name=role_name)
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)

# Sends message with reactions
@client.command()
async def react(ctx):
    message = "React to this message to get a role!"
    react_message = await ctx.send(message)
    for emoji in emoji_roles:
        await react_message.add_reaction(emoji=emoji)




client.run(TOKEN)