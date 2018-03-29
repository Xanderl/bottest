#thisa big boi by xander


import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio

bot = commands.Bot(command_prefix='#')



@bot.event
async def on_ready():
    print ("ready for use, just gunna add a happy syntax error here")
    print (bot.user.id)

#this is the basic template for bot commands "meme" is the command word
@bot.command(pass_context=True)
async def meme(ctx):
    await bot.say("I like memes")
#for info use #info username
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The username is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("the users highest role is: {}".format(user.top_role))
    await bot.say("the user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def intro(ctx):
    await bot.say("#info username   -get users info")
    await bot.say("#kick username  -kick a user")
    await bot.say(" use # to start a command")

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say("{} was not worthy".format(user.name))
    await bot.kick(user)




#this is the basic template for checking is a word is in a message and sending a message, the message that the bot replys with can NOT have the word that it is checking for in it.
@bot.event
async def on_message(message):
    if 'never' in message.content:
        await bot.send_message(message.channel, 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
#anything indented is part of the if statement reamember to indent only half way so that the process commands is always running
    await bot.process_commands(message)



#this needs to be at the bottom of the script
bot.run("NDI4NjEzOTAzOTY3MzIyMTEy.DZ2PxA.wTjxxeVd2LsTCuNMnDn-hEcoBxI")
