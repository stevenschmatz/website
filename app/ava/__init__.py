from communication import *
from cron import add_cron_jobs


def launch_bot():
    if not sc.rtm_connect():
        print "Connection failed on Ava init"
        return


add_cron_jobs()
