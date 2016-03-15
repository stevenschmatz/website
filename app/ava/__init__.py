
from communication import *


def launch_bot():
    if not sc.rtm_connect():
        print "Connection failed on Ava init"
        return

    send_me("Hello Steven!")
