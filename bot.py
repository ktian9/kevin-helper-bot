# bot.py
import os

import discord


import json

f = open("tokens.json")
TOKEN = json.load(f)['discord']
f.close()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
