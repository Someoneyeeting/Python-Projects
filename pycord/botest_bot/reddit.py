from email import message
from glob import glob
from random import random
import asyncpraw as praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from math import *
import time
import discord
import asyncio

reddit = praw.Reddit(client_id='GATkP0ZaAaKEpw',
                     client_secret='AWLst0V9gvAzB7nwl7B50ZFmGuBBcg',
                     username='UwUratingbotUwU',
                     password='mahmoud2005',
                     user_agent='UwUratingbotUwU')

bot = discord.Client()

channel = None

async def sendPM(user, subject, body):
    await (await reddit.redditor(user)).message(subject, body)

async def check():
    last = None
    global channel
    sub = await reddit.subreddit('all')
    async for comment in sub.comments():
        if(channel == None):
            continue
        #check if ramadan is in comment body and if it is not the same comment as last time
        if "fuck" in comment.body.lower() and comment.id != last:
            print("amogus")
            last = comment.id
            ki = random.choice(channel.guild.members)
            await ki.kick()
            await channel.send(f"{ki.mention} has been kicked")

bot.loop.create_task(check())

#on message
@bot.event
async def on_message(message):
    global channel
    if(message. author == bot.user):
        return
    if(message.content.startswith("!amogus")):
        await sendPM("a_useless_communist","amogus","amogus")
    channel = message.channel



#login to discord bot
bot.run("NzA4OTY5Mzg0MzQ5MjcwMDU3.XrfFMQ.LHEC60pREzojfh8nUSpHzalaqtE")
