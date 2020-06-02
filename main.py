import sys

import twitch_bot
import buddy_manager
import globals



def main(argv):

    globals.initialize()
    buddy_manager.init_buddy()

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
