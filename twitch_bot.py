from twitchio.ext import commands
import asyncio
import logging
import globals
import py3buddy

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
async def test_command(ctx):
    await ctx.send("You can change The i-Buddy state by send command in tchat !left / !right / !wing high / !wing low ")

@bot.command(name='buddy')
async def test_command(ctx):
    print("Demo 4: Executing commands\n")
    cmds = ["WHITE:WINGSHIGH:HEART:GO:SLEEP",
            "RED:WINGSLOW:GO:SLEEP:NOHEART:LEFT:GO:SLEEP:RESET",
            "::BLUE:GO:SHORTSLEEP"]
    for cmd in cmds:
        print("Executing: ", cmd)
        globals.ibuddy.executecommand(cmd)
    #globals.ibuddy.reset()
    await ctx.send('Hello')

@bot.command(name='left')
async def left_command(ctx):
    globals.ibuddy.wiggle("left")
    globals.ibuddy.sendcommand()

@bot.command(name='right')
async def right_command(ctx):
    globals.ibuddy.wiggle("right")
    globals.ibuddy.sendcommand()

@bot.command(name='middle')
async def middle_command(ctx):
    globals.ibuddy.wiggle("middle")
    globals.ibuddy.sendcommand()

@bot.command(name='wing')
async def wing_command(ctx):
    cmds = ctx.content.split(' ')[-1]
    print(cmds)
    if cmds in ['high', 'low']:
        globals.ibuddy.wings(cmds)
        globals.ibuddy.sendcommand()

    else:
        await ctx.send("Bad argument")

@bot.command(name='cmd')
async def cmd_command(ctx):
    cmds = ctx.content.split()
    for cmd in cmds:
        print("Executing: ", cmd)
        globals.ibuddy.executecommand(cmd)
    globals.ibuddy.reset()

