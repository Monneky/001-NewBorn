import discord
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

@client.event
async def on_member_join(member):
    privateChannel = await member.create_dm()
    await privateChannel.send(f'Hey {member} I am 001-New Born, I\'m a simple bot, I\'m here to help you in all things you need in the future.')
    await privateChannel.send(f'Actually I\'m a bot of the serie New Born, I\'m not only bots of discord, In the future my creators are planning to crete more, so enjoy the channel')

client.run(TOKEN)