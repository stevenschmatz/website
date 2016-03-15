import os
from slackclient import SlackClient
from app import config

sc = SlackClient(os.environ.get("SLACK_BOT_TOKEN") or
                 config['slack']['bot_token'])

PERSONAL_CHAT_CHANNEL_ID = "D0SGBC3HB"


def send_me(message):
    """Sends my personal Slack chat a message."""
    sc.rtm_send_message(PERSONAL_CHAT_CHANNEL_ID, message)
