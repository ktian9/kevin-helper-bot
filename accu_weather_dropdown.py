import discord

class AccuDropdown(discord.ui.Select):
    def __init__(self, location_list):

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
        
        await interaction.response.send_message(f'Selected location is {self.values[0]}')
        global selected_value
        selected_value = self.values[0]
        
        ## need to insert into database
        return self.values[0]
    
    async def get_current_value(self):
        return selected_value


class AccuDropdownView(discord.ui.View):
    def __init__(self, location_list):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(AccuDropdown(location_list))
        