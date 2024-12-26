import discord
import os
from dotenv import load_dotenv

# TOKEN ACCESS
load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

# EVENTS

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('hello'):
            await message.channel.send(f'Hi there {message.author}!')

# INTENTS
intents = discord.Intents.default()
intents.message_content = True

# RUN

client = Client(intents=intents)
client.run(discord_token)
