#setup discord bot and start it


import discord
import asyncio
import os
import sys
import time
import json
import random
import requests
import re


#setup discord bot
client = discord.Client()


#setup discord bot
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    


#setup discord bot
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    #if message.content.startswith('!hello'):
    #    msg = 'Hello {0.author.mention}'.format(message)
    #    await client.send_message(message.channel, msg)

    if message.content.startswith('!help'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!copilot'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!copilot'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!copilot'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!copilot'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!copilot'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!copilot'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!copilot'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!copilot'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)


#login in to bot
client.run(os.environ['BOT_TOKEN'])