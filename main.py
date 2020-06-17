import sys

import globals

import buddy_manager
import twitch_bot

def main(argv):
    globals.initialize()
    buddy_manager.init_buddy()

    twitch_bot.run()

    #ws_client.stsrv()

    buddy_manager.panic(10)
'''
    print("Demo 4: Executing commands\n")
    cmds = ["WHITE:LEFT:HEART:GO:SLEEP","RED:RIGHT:GO:SLEEP:NOHEART::GO:SLEEP:RESET","::BLUE:MIDDLE:GO:SHORTSLEEP"]
    for cmd in cmds:
        print("Executing: ", cmd)
        globals.ibuddy.executecommand(cmd)
    globals.ibuddy.reset()

'''


if __name__ == "__main__":
    main(sys.argv)

    print("Test")
