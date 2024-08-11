import discord
from discord.ext import commands
import api_query
from datetime import datetime
from PIL import Image
import os, os.path

imgs = []
path = "./weather_icons"
valid_images = [".jpg",".gif",".png",".tga"]

    

   
class AccuDropdown(discord.ui.Select):
    def __init__(self, location_list, height):

        global cloud_ceiling_height
        global location_as_list
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
    

class AccuDropdownView(discord.ui.View):
    def __init__(self, location_list, height):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(AccuDropdown(location_list, height))
        