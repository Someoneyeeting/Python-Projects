import discord
import math
import random
import asyncio

bot = discord.Client()


amogus = ""
async def sendMessage(channel,message):
    await channel.send(message)

async def sendPM(user,message):
    await user.dm_channel.send(message)

#read amogus and sotre it in amogus varable
with open('copypasta.txt') as f:
    #add copypasta.txt to amogus line by line
    for line in f:
    #     x = ""
    #     for l in line:
    #         #if l is an ascoii char
    #         if ord(l) < 128:
    #             x += l
    #     if(x != ""):
    #         print(x)
        amogus += line + "\n"


#loop through amogus and check if it has an emoji and convert it to discord emoji
def convertEmoji(message):
    pass
    

async def jojo(channel):
    line = 0
    while True:
        await sendMessage(channel,amogus)
        # try:
        #     if(amogus[line] != ""):
        #         await sendMessage(channel,amogus[line])
        # except Exception as e:
        #     print(e)
        # line +=1
        # if(line >= len(amogus)):
        #     break

        await asyncio.sleep(0.2)


#on message
@bot.event
async def on_message(message):
    global pongs
    #check if its a private message
    if message.author == bot.user:
        return
    if("amogus" in message.content.lower()):
        bot.loop.create_task(jojo(message.channel))

bot.run("NzUyNDY4NDUyNDU0OTU3MDg3.X1YE2w.FGpALWB_IGm0iXQ62SrlIFLH5pE")
