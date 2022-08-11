import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

channel = None
spamming = ""

async def spam():
    global channel,spamming
    while True:
        if(channel != None):
            await channel.send(spamming)
        await asyncio.sleep(0.1)

@client.event
async def on_message(message):
    global channel,spamming
    if message.author == client.user:
        return

    if message.content.startswith('start'):
        channel = message.channel
        spamming = message.mentions[0].mention

client.loop.create_task(spam())

client.run('NzA4OTY5Mzg0MzQ5MjcwMDU3.XrfFMQ.LHEC60pREzojfh8nUSpHzalaqtE')