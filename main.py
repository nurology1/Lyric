import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

# ENV-ACCESS
load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')
dev_server_id = os.getenv('DEV_SERVER_ID') # In the .env file, below the "DISCORD_TOKEN" add your own development server id after stating "DEV_SERVER_ID" if you choose to add more objects into the code.

# MISC
guild = discord.Object(id=dev_server_id) 

# EVENTS
class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        await client.change_presence(activity=discord.Game(name='Being Developed...'))

        # COMMAND-SYNC
        try:
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')

        except Exception as e:
            print(f'Error syncing commands: {e}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('hello'):
            await message.channel.send(f'Hello there {message.author}!')

    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('You reacted!')

# INTENTS
intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix=".", intents=intents)

# DEV-SLASH-COMMANDS
@client.tree.command(name="hello_world_dev", description='Saying "Hello World!" (Development)', guild=guild)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello World!")
@client.tree.command(name="print_dev", description="Passing Through What You Say! (Development)", guild=guild)
async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)
    
# RUN
client.run(discord_token)
