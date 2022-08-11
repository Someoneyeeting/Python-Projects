import discord
import bot2


client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await bot2.on_message(message,client)
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

client.run('NzA4OTY5Mzg0MzQ5MjcwMDU3.XrfFMQ.LHEC60pREzojfh8nUSpHzalaqtE')