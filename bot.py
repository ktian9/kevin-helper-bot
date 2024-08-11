# https://embed.dan.onl/
import os
from datetime import datetime
import discord
from discord.ext import commands
import requests
import json
import accu_weather_dropdown
import api_query


### Loading Tokens
f = open("tokens.json")
file = json.load(f)
TOKEN = file['discord']
accu_TOKEN = file['accuweather']
f.close()



### Initial Discord Generation
intents = discord.Intents.default()
intents.message_content = True
# client = discord.Client(intents=intents)
client = commands.Bot(command_prefix = "!sorairo ", intents=intents)



### Loading Database



@client.event
async def on_ready():
    game = discord.Game("Kevin's personal discord helper")
    await client.change_presence(status = discord.Status.online, activity=game)
    print(f'{client.user} has connected to Discord!')
    
    

@client.command()
async def register_cloud_inversion(client, *message):
    try:
        location = " ".join(message[1:])
        height = message[0]
        
        items = await api_query.query_accuweather_location_details(location)
        print(items)
        location_list = []
        for i in items:
            loc_dict = {'key': i['Key'], 'location': i['LocalizedName'], 'country': i['Country']['LocalizedName'], 'state': i['AdministrativeArea']['ID']}
            location_list.append(loc_dict)
            
            
            
        view = accu_weather_dropdown.AccuDropdownView(location_list, height)
        
        
        embed = discord.Embed(title="Please select the location below",
                      url="https://www.accuweather.com/",
                      description="> Please make sure that the location exists on accuweather and utilize the proper name here\n[Accuweather](https://www.accuweather.com/)",
                      colour=0x8080c0,
                      timestamp=datetime.now())
        embed.set_author(name="Cloud Inversion Location Selector")
        embed.set_thumbnail(url="https://www.verizon.com/about/sites/default/files/news-media/150310_AccuWeather_640x400.jpg")

        embed.set_footer(text="kevin's personal discord bot",
                 icon_url="https://slate.dan.onl/slate.png")
        
        await client.send(embed = embed, view = view)
        
        
        
        
        
        
        
        
        
        
            
    except Exception as e:
        print("main bot thread exception")
        print(e)
        
      

client.run(TOKEN)
