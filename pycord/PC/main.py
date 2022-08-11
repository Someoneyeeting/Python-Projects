#setup new discord bot
import discord
from discord.ext import commands
import asyncio
import random
import os
import json

#new bot with no command prefix
bot = commands.Bot(command_prefix='')

#new slash command /send to send a message to a user

me = 0
#on private message
@bot.event
async def on_message(message):
	global me
	#check if its a private message
	if message.author == bot.user:
		return
	if(isinstance(message.channel,discord.channel.DMChannel)):
		if(message.content.startswith('shutdown')):
			#shutdown pc
			sendPM(message.author,'Shutting down')
			os.system('shutdown -s -t 3')
		if(message.content.startswith("set")):
			me = message.author
		if(me != 0):
			sendPM(me,message.content)
	if(message.content.startswith("send")):
		#check if it has mentions
		if(message.mentions):
			#send message to mentioned user
			messag = ""
			for i in message.content.split(" ")[2::]:
				messag += i + " "
			await sendPM(message.mentions[0],messag)
			#remove message
			await message.delete()

	
#setup bot token from configuraton.json file
with open('configuration.json') as json_file:
	data = json.load(json_file)
	bot_token = data['token']

async def sendPM(user,message):
	#get user from name
	await user.dm_channel.send(message)



#login to bot
bot.run(bot_token)