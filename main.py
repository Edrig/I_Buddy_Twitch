import sys
import os
import argparse
import configparser
import random
import time

import config
import py3buddy

import twitch_bot
import globals

def init_buddy():

    buddy_config = {'productid': int(config.productid), 'reset_position': config.reset_position}

    # initialize an iBuddy and check if a device was found and is accessible
    ibuddy = py3buddy.iBuddy(buddy_config)
    globals.ibuddy = ibuddy
    if ibuddy.dev is None:
        print("No iBuddy found, or iBuddy not accessible", file=sys.stderr)
        sys.exit(1)

def panic(ibuddy, paniccount):
    # a demo version to show some of the capabilities of the iBuddy

    # first reset the iBuddy
    ibuddy.reset()
    for i in range(0, paniccount):
        # set the wings to high
        ibuddy.wings('high')

        # turn on the heart LED
        ibuddy.toggleheart(True)

        # pick a random colour for the head LED
        ibuddy.setcolour(random.choice(py3buddy.allcolours))

        # wiggle randomly
        ibuddy.wiggle(random.choice(['right', 'left', 'middle', 'middlereset']))

        # create the message, then send it, and sleep for 0.1 seconds
        ibuddy.sendcommand()
        time.sleep(0.1)

        # set the wings to low
        ibuddy.wings('low')

        # turn off the heart LED
        ibuddy.toggleheart(False)

        # pick a random colour for the head LED
        ibuddy.setcolour(random.choice(py3buddy.allcolours))

        # random wiggle
        ibuddy.wiggle(random.choice(['right', 'left', 'middle', 'middlereset']))
        ibuddy.sendcommand()
        time.sleep(0.1)

    # extra reset as sometimes the device doesn't respond
    ibuddy.reset()
    ibuddy.reset()

def main(argv):

    globals.initialize()
    init_buddy()

'''
    print("Demo 4: Executing commands\n")
    cmds = ["WHITE:WINGSHIGH:HEART:GO:SLEEP",
            "RED:WINGSLOW:GO:SLEEP:NOHEART:LEFT:GO:SLEEP:RESET",
            "::BLUE:GO:SHORTSLEEP"]
    for cmd in cmds:
        print("Executing: ", cmd)
        globals.ibuddy.executecommand(cmd)
    globals.ibuddy.reset()
'''

if __name__ == "__main__":

    main(sys.argv)
    twitch_bot.bot.run()
