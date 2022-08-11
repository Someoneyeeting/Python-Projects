#setup import discord bot
import asyncio
import discord
import random

#tell me programming jokes
#

#login to discord bot with te token in token.txt
client = discord.Client()



#shuffle a string
def shuffle(string):
    import random
    string = list(string)
    random.shuffle(string)
    return ''.join(string)

#send message with message.channel.send
async def send_message(message, message_to_send):
    await message.channel.send(message_to_send)

#create a new role in guild
async def create_role(message, role_name):
    guild = message.guild
    await guild.create_role(name=role_name)

#if someone send !play join the same voice channel
async def join_voice_channel(message):
    voice_channel = message.author.voice.channel
    if voice_channel is not None:
        voice_client = await voice_channel.connect()
        return voice_client
    else:
        await send_message(message, "You need to be in a voice channel to use this command")



#run the bot with the token in token.txt
client.run(open('token.txt', 'r').read())