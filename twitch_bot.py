from twitchio.ext import commands
import asyncio
import logging
import globals
import py3buddy
import buddy_manager
import time

import threading

from config import *

bot = commands.Bot(
    irc_token=TMI_TOKEN,
    client_id=CLIENT_ID,
    nick=BOT_NICK,
    prefix=BOT_PREFIX,
    initial_channels=CHANNEL
)

#logging.basicConfig(filename='log.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

# Register an event with the bot
@bot.event
async def event_ready():
    print(f'Ready | {bot.nick}')

@bot.event
async def event_message(message):
    print('%s: %s' % (message.author.name,message.content))

    if message.author.name.lower() == "Edrig_bot":
        return
    # If you override event_message you will need to handle_commands for commands to work.
    logging.info('Msg From: %s ' %(message.author))
    await bot.handle_commands(message)


@bot.command(name='help')
async def help_command(ctx):
    await ctx.send("You can change The i-Buddy state by send command in tchat !buddy / !wing (high,low) / !heart (True/False)")

@bot.command(name='aide')
async def aide_command(ctx):
    await ctx.send("Tu peux me contrôler en ecrivant dans le Tchat !buddy / !wing (high,low) / !heart (True/False)")

@bot.command(name='status')
async def status_command(ctx):
    await ctx.send(buddy_manager.get_status())

@bot.command(name='buddy')
async def buddy_command(ctx):
    print("Demo 4: Executing commands\n")
    cmds = ["WHITE:WINGSHIGH:HEART:GO:SLEEP",
            "RED:WINGSLOW:GO:SLEEP:NOHEART:LEFT:GO:SLEEP:RESET",
            "::BLUE:GO:SHORTSLEEP"]
    for cmd in cmds:
        print("Executing: ", cmd)
        globals.ibuddy.executecommand(cmd)
    #globals.ibuddy.reset()
    #await ctx.send('Hello')

@bot.command(name='left')
async def left_command(ctx):
    globals.ibuddy.wiggle("right")
    globals.ibuddy.sendcommand()

@bot.command(name='right')
async def right_command(ctx):
    globals.ibuddy.wiggle("left")
    globals.ibuddy.sendcommand()

@bot.command(name='middle')
async def middle_command(ctx):
    globals.ibuddy.wiggle("middle")
    globals.ibuddy.sendcommand()

@bot.command(name='wing')
async def wing_command(ctx):
    cmd = ctx.content.split(' ')[-1]
    print(cmd)

    if cmd == '!wing':
        #await ctx.send("Missing argument")
        if globals.wing == "high":
            globals.ibuddy.wings("low")
            globals.ibuddy.sendcommand()
            globals.wing = "low"
        elif globals.wing == "low":
            globals.ibuddy.wings("high")
            globals.ibuddy.sendcommand()
            globals.wing = "high"

'''
    if cmd in ['high', 'low']:
            globals.ibuddy.wings(cmd)
            globals.ibuddy.sendcommand()
    else:
        await ctx.send("Bad argument")
'''


@bot.command(name='heart')
async def heart_command(ctx):
    cmd = ctx.content.split(' ')[-1]
    #print(cmd)
    #print("Test: %s " %(globals.heart))
    if cmd == '!heart':
        if globals.heart == "True":
            globals.ibuddy.toggleheart(False)
            globals.ibuddy.sendcommand()
            globals.heart = "False"
        elif globals.heart == "False":
            globals.ibuddy.toggleheart(True)
            globals.ibuddy.sendcommand()
            globals.heart = "True"

    if cmd == 'True' or cmd == 'true':
        globals.ibuddy.toggleheart(True)
        globals.ibuddy.sendcommand()
        globals.heart = "True"
    elif cmd == 'False' or cmd == 'false':
        globals.ibuddy.toggleheart(False)
        globals.ibuddy.sendcommand()
        globals.heart = "False"



@bot.command(name='color')
async def color_command(ctx):

    cmd = ctx.content.split(' ')[-1]
    color = cmd.upper()
    if color == "BLACK":
        print("iBuddy chose: no colour!\n")
        globals.ibuddy.setcolour(py3buddy.NOCOLOUR)
        globals.ibuddy.sendcommand()
    if color == "NOCOLOUR":
        print("iBuddy chose: no colour!\n")
        globals.ibuddy.setcolour(py3buddy.NOCOLOUR)
        globals.ibuddy.sendcommand()
    elif color == "RED":
        print("iBuddy chose: red!\n")
        globals.ibuddy.setcolour(py3buddy.RED)
        globals.ibuddy.sendcommand()
    elif color == "BLUE":
        print("iBuddy chose: blue!\n")
        globals.ibuddy.setcolour(py3buddy.BLUE)
        globals.ibuddy.sendcommand()
    elif color == "GREEN":
        print("iBuddy chose: green!\n")
        globals.ibuddy.setcolour(py3buddy.GREEN)
        globals.ibuddy.sendcommand()
    elif color == "CYAN":
        print("iBuddy chose: cyan!\n")
        globals.ibuddy.setcolour(py3buddy.CYAN)
        globals.ibuddy.sendcommand()
    elif color == "YELLOW":
        print("iBuddy chose: yellow!\n")
        globals.ibuddy.setcolour(py3buddy.YELLOW)
        globals.ibuddy.sendcommand()
    elif color == "PURPLE":
        print("iBuddy chose: purple!\n")
        globals.ibuddy.setcolour(py3buddy.PURPLE)
        globals.ibuddy.sendcommand()
    elif color == "WHITE":
        print("iBuddy chose: white!\n")
        globals.ibuddy.setcolour(py3buddy.WHITE)
        globals.ibuddy.sendcommand()
    #if cmd in ['nocolour', 'red', 'blue', 'green','cyan', 'yellow', 'purple', 'white']:
    #print(cmd.upper())
    #globals.ibuddy.setcolour(py3buddy.RED)
    #globals.ibuddy.sendcommand()

@bot.command(name='rainbow')
async def rainbow_command(ctx):
    buddy_manager.colourloop(1)

@bot.command(name='panic')
async def panic_command(ctx):

    buddy_manager.panic(10)

@bot.command(name='flap')
async def flap_command(ctx):

    buddy_manager.flaploop(10)

# WHITE:WINGSHIGH:HEART:GO:SLEEP",
# RED:WINGSLOW:GO:SLEEP:NOHEART:LEFT:GO:SLEEP:RESET:BLUE:GO:SHORTSLEEP
@bot.command(name='cmd')
async def cmd_command(ctx):
    cmds = ctx.content.split()
    for cmd in cmds:
        print("Executing: ", cmd)
        globals.ibuddy.executecommand(cmd)
    globals.ibuddy.reset()

def run():
    print("Starting Twitch Bot")
    bot.run()