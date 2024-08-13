import discord
from discord.ext import commands
import api_query
from datetime import datetime
from PIL import Image
import os, os.path
import psycopg2
import sys
sys.path.insert(0, "./database")
import database_accuweather
imgs = []
path = "./weather_icons"
valid_images = [".jpg",".gif",".png",".tga"]

    

   
class AccuDropdown(discord.ui.Select):
    def __init__(self, location_list, height, in_channel_id):

        global cloud_ceiling_height
        global location_as_list
        global channel_id
        channel_id = channel_id
        location_as_list = location_list
        cloud_ceiling_height = height

        # Set the options that will be presented inside the dropdown
        options = []
        for i in location_list:
            option = discord.SelectOption(label= i['location'], description= i['country'] + " - " +  i['state'], value = i['key'])
            options.append(option)
            
        print(location_list)

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(placeholder='Choose your location...', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        # selected options. We only want the first one.
        
        global selected_value
        selected_value = self.values[0]
        selected_location = {}
        for i in location_as_list:
            if i['key'] == selected_value:
                selected_location = i
        

        current_conditions = await api_query.query_accuweather_current_conditions(selected_location['key'])
        print(current_conditions)
        is_possible = "Not Possible"
        if(float(current_conditions['cloud_cover']) < float(cloud_ceiling_height)):
            is_possible = "Possible"
           

        embed = discord.Embed(title="Weather Details",
                      colour=0x00b0f4,
                      timestamp=datetime.now())

        embed.set_author(name="Weather Information",
                        url=current_conditions['link'])

        embed.add_field(name="Weather Description",
                        value=current_conditions['weather_description'],
                        inline=False)
        embed.add_field(name="Is Raining",
                        value=current_conditions['is_raining'],
                        inline=True)
        embed.add_field(name="Rain Type",
                        value=current_conditions['rain_type'],
                        inline=True)
        embed.add_field(name="Humidity",
                        value=current_conditions['humidity'],
                        inline=True)
        embed.add_field(name="Temperature",
                        value=current_conditions['temperature'],
                        inline=True)
        embed.add_field(name="Feeling",
                        value=current_conditions['feeling'],
                        inline=True)
        embed.add_field(name="Windchill",
                        value=current_conditions['windchill'],
                        inline=True)
        embed.add_field(name="Cloud Clover",
                        value=current_conditions['cloud_cover'],
                        inline=True)
        embed.add_field(name="Cloud Inversion",
                        value=is_possible,
                        inline=True)
        embed.add_field(name="Visibility Obstruction",
                        value=current_conditions['obstructions_to_visibility'],
                        inline=True)
        # img = (Image.open(os.path.join(path,str(current_conditions['weather_icon']) +str(".png")))))
        file_name = 'weather_icons/' + str(current_conditions['weather_icon']) + ".png"
        file = discord.File(file_name)  
        embed.set_thumbnail(url=f"attachment://{file.filename}")
        # embed.set_thumbnail(url=current_conditions['weather_icon'])

        # await ctx.send(embed=embed)
        

        await interaction.response.send_message(embed=embed, file = file)
        
        ## need to insert into database
        # _ = selected_location[0]['state'] + " " + selected_location[0]['country']
        # await interaction.response.send_message(f'Selected location is {_}')
        
        database_dict = {
            "weather_description": current_conditions['weather_description'],
            "is_raining": current_conditions['is_raining'],
            "rain_type": current_conditions['rain_type'],
            "humidity": current_conditions['humidity'],
            "temperature": current_conditions['temperature'],
            "feeling": current_conditions['feeling'],
            "windchill": current_conditions['windchill'],
            "cloud_cover": current_conditions['cloud_cover'],
            "cloud_inversion": is_possible,
            "visibility_obstruction": current_conditions['obstructions_to_visibility'],
            "accu_key": selected_location['key'],
            "tracked_state": selected_location['state'],
            "tracked_country": selected_location['country'],
            "tracked_name": selected_location['location'],
            "user_submitted": interaction.user.global_name, ## from interactoin
            "date_updated": datetime.today().strftime('%Y-%m-%d'), ## current date
            "date_registered": datetime.today().strftime('%Y-%m-%d'),   ## current date          
        }
        
        print(database_accuweather.insert_into_weathertable(database_dict))
        # weather_description = query_params['weather_description']
        # is_raining = query_params['is_raining']
        # rain_type = query_params['rain_type']
        # humidity = query_params['humidity']
        # temperature = query_params['temperature']
        # feeling = query_params['feeling']
        # windchill = query_params['windchill']
        # cloud_cover = query_params['cloud_cover']
        # cloud_inversion = query_params['cloud_inversion']
        # visibility_obstruction = query_params['visibility_obstruction']
        # accu_key = query_params['accu_key']
        # tracked_state = query_params['tracked_state']
        # tracked_country = query_params['tracked_country']
        # tracked_name = query_params['tracked_name']
        # user_submitted = query_params['user_submitted']
        # date_updated = query_params['date_updated']
        # date_registered = query_params['date_registered']

class AccuDropdownView(discord.ui.View):
    def __init__(self, location_list, height, channel_id):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(AccuDropdown(location_list, height, channel_id))
        