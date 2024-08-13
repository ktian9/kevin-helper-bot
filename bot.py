# https://embed.dan.onl/
import os
import datetime
import discord
from discord.ext import commands, tasks
import requests
import json
import accu_weather_dropdown
import api_query
from pytz import timezone
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import database_accuweather
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
bot = commands.Bot(command_prefix = "!sorairo ", intents=intents)



### Loading Database


@bot.event
async def send_cloud_inversion_details():
    await bot.wait_until_ready()
    c = bot.get_channel(437010005149876229)
    
    active_channels = database_accuweather.get_active_channels()
    
    for i in active_channels():
            
    
    
    
    
    
    
    
    
    
    await c.send("testing triggered message")
    
    
    
    
@bot.event
async def on_ready():
    game = discord.Game("Kevin's personal discord helper")
    await bot.change_presence(status = discord.Status.online, activity=game)

    
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_cloud_inversion_details, CronTrigger(hour=17, minute=26))
    scheduler.start()
    print(f'{bot.user} has connected to Discord!')
    
    

@bot.command()
async def register_cloud_inversion(client, *message):
    try:
        location = " ".join(message[2:])
        print(f"location: {location}")
        height = message[0]
        print(f"height: {height}")
        channel_id = message[1]
        print(f"channel_id: {channel_id}")

        items = await api_query.query_accuweather_location_details(location)
        #print(items)
        location_list = []
        for i in items:
            loc_dict = {'key': i['Key'], 'location': i['LocalizedName'], 'country': i['Country']['LocalizedName'], 'state': i['AdministrativeArea']['ID']}
            location_list.append(loc_dict)
            
            
            
        view = accu_weather_dropdown.AccuDropdownView(location_list, height, channel_id)
        
        
        embed = discord.Embed(title="Please select the location below",
                      url="https://www.accuweather.com/",
                      description="> Please make sure that the location exists on accuweather and utilize the proper name here\n[Accuweather](https://www.accuweather.com/)",
                      colour=0x8080c0,
                      timestamp=datetime.datetime.now())
        embed.set_author(name="Cloud Inversion Location Selector")
        embed.set_thumbnail(url="https://www.verizon.com/about/sites/default/files/news-media/150310_AccuWeather_640x400.jpg")

        embed.set_footer(text="kevin's personal discord bot",
                 icon_url="https://slate.dan.onl/slate.png")
        
        await client.send(embed = embed, view = view)
        
                
        
        
        
        
        
        
            
    except Exception as e:
        print("main bot thread exception")
        print(e)





bot.run(TOKEN)
