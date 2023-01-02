#Import the libraries
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# defining the prefix
prefix = '$'
# Charge all the .env files to read the TOKEN for our bot
load_dotenv()
# getting the token
TOKEN = os.getenv('TOKEN')
intents = discord.Intents.default()
intents.message_content = True

# defining the bot with the prefix
bot = commands.Bot(command_prefix=prefix, intents=intents)
# removing the command help to stablish one custome
bot.remove_command('help')

# --------------- When the bot is ready -----------------------
@bot.event
async def on_ready():
    print(f'Logged in {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

@bot.event
async def on_member_join(member):
    privateChannel = await member.create_dm()
    await privateChannel.send(f'Hey {member} I am 001-New Born, I\'m a simple bot, I\'m here to help you in all things you need in the future.')
    await privateChannel.send(f'Actually I\'m a bot of the serie New Born, I\'m not only bots of discord, In the future my creators are planning to crete more, so enjoy the channel')

bot.run(TOKEN)