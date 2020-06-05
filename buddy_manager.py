import sys
import random
import time

import config
import py3buddy
import globals


def init_buddy():

    buddy_config = {'productid': int(config.productid), 'reset_position': config.reset_position}

    # initialize an iBuddy and check if a device was found and is accessible
    ibuddy = py3buddy.iBuddy(buddy_config)
    globals.ibuddy = ibuddy
    if ibuddy.dev is None:
        print("No iBuddy found, or iBuddy not accessible", file=sys.stderr)
        sys.exit(1)

def panic(paniccount):
    # a demo version to show some of the capabilities of the iBuddy

    # first reset the iBuddy
    globals.ibuddy.reset()
    for i in range(0, paniccount):
        # set the wings to high
        globals.ibuddy.wings('high')

        # turn on the heart LED
        globals.ibuddy.toggleheart(True)

        # pick a random colour for the head LED
        globals.ibuddy.setcolour(random.choice(py3buddy.allcolours))

        # wiggle randomly
        globals.ibuddy.wiggle(random.choice(['right', 'left', 'middle', 'middlereset']))

        # create the message, then send it, and sleep for 0.1 seconds
        globals.ibuddy.sendcommand()
        time.sleep(0.1)

        # set the wings to low
        globals.ibuddy.wings('low')

        # turn off the heart LED
        globals.ibuddy.toggleheart(False)

        # pick a random colour for the head LED
        globals.ibuddy.setcolour(random.choice(py3buddy.allcolours))

        # random wiggle
        globals.ibuddy.wiggle(random.choice(['right', 'left', 'middle', 'middlereset']))
        globals.ibuddy.sendcommand()
        time.sleep(0.1)

    # extra reset as sometimes the device doesn't respond
    globals.ibuddy.reset()
    globals.ibuddy.reset()

def colourloop(loopcount):
    globals.ibuddy.reset()
    for i in range(0, loopcount):
        for c in py3buddy.allcolours:
            globals.ibuddy.setcolour(c)
            globals.ibuddy.sendcommand()
            time.sleep(1)
    globals.ibuddy.reset()
    globals.ibuddy.reset()

def flaploop(loopcount):
    globals.ibuddy.reset()
    for i in range(0, loopcount):

        # set the wings to high
        globals.ibuddy.wings('high')
        globals.ibuddy.sendcommand()
        time.sleep(0.1)

        globals.ibuddy.wings('low')
        globals.ibuddy.sendcommand()
        time.sleep(0.1)