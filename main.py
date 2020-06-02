import sys
import os
import argparse
import configparser
import random
import time
import py3buddy

import twitch_bot
import globals
ibuddy_instance = ""

def init_buddy(argv):
    parser = argparse.ArgumentParser()

    # options for the commandline
    parser.add_argument("-c", "--config", action="store", dest="cfg",
                        help="path to configuration file", metavar="FILE")
    args = parser.parse_args()

    # first some sanity checks for the configuration file
    if args.cfg is None:
        parser.error("Configuration file missing")

    if not os.path.exists(args.cfg):
        parser.error("Configuration file does not exist")

    # then parse the configuration file
    config = configparser.ConfigParser()

    configfile = open(args.cfg, 'r')

    try:
        config.readfp(configfile)
    except Exception:
        print("Cannot read configuration file", file=sys.stderr)
        sys.exit(1)

    buddy_config = {}
    for section in config.sections():
        if section == 'ibuddy':
            try:
                productid = int(config.get(section, 'productid'))
                buddy_config['productid'] = productid
            except:
                pass

            buddy_config['reset_position'] = False
            try:
                reset_position_val = config.get(section, 'reset_position')
                if reset_position_val == 'yes':
                    buddy_config['reset_position'] = True
            except:
                pass

    # initialize an iBuddy and check if a device was found and is accessible
    ibuddy_instance = py3buddy.iBuddy(buddy_config)
    globals.ibuddy = ibuddy_instance
    if ibuddy_instance.dev is None:
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
    init_buddy(argv)

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
