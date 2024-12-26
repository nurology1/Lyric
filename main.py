import discord
import os
from dotenv import load_dotenv

# TOKEN ACCESS
load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        print(f'Message Detected. "{message.author}: {message.content}"')


intents = discord.Intents.default()
intents.message_content = True


client = Client(intents=intents)
client.run(discord_token)
