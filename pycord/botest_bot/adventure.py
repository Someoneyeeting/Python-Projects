import discord
from discord.ext import commands
import asyncio
import random

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("start")

among = "WHEN THE IMPOSTER IS SUS-sus-amogus-GETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEAD-STOP POSTING ABOUT AMONG US".split("-")


async def target(t):
    while(True):
        await t.send(random.choice(among))
        await asyncio.sleep(0.01)
    

@bot.event
async def on_message(message):
    if(message.author == bot.user):
        return
    if(message.content.lower() == "sus"):
        bot.loop.create_task(target(message.author))
        
    

bot.run("NzA4OTY5Mzg0MzQ5MjcwMDU3.XrfFMQ.LHEC60pREzojfh8nUSpHzalaqtE")
