import os
import discord
from common import config
from commands import standard_replies

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    await standard_replies.reply_to_message(message)

client.run(os.getenv('DISCORD_TOKEN'))
