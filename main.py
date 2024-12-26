import discord
import os
from dotenv import load_dotenv

# TOKEN ACCESS
load_dotenv()
TOKEN = os.getenv("TOKEN")

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logging on as {self.user}')

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run('TOKEN')
