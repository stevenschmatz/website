import os
from slackclient import SlackClient
from app import config
from api.pomodoro import work_summary_english

sc = SlackClient(os.environ.get("SLACK_BOT_TOKEN") or
                 config['slack']['bot_token'])
ME = "D0SGBC3HB"


def launch_bot():
    if not sc.rtm_connect():
        print "Connection failed on Ava init"
        return

    sc.rtm_send_message(ME, work_summary_english())
