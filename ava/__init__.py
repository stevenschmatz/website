import os
import datetime
from slackclient import SlackClient
from app import db, config
from app.weather import get_weather_description

sc = SlackClient(os.environ.get("SLACK_BOT_TOKEN") or
                 config['slack']['bot_token'])
ME = "D0SGBC3HB"


def launch_bot():
    if not sc.rtm_connect():
        print "Connection failed on Ava init"
        return

    weather_description = get_weather_description()
    message = "Good morning! {0}".format(weather_description)
    sc.rtm_send_message("general", message)

    now = datetime.datetime.utcnow()
    yesterday = now - datetime.timedelta(days=1)
    last_week = now - datetime.timedelta(days=7)

    pomodoros_day = db.pomodoro.find({"time": {"$lt": now,
                                               "$gt": yesterday}}).count()
    pomodoros_week = db.pomodoro.find({"time": {"$lt": now,
                                                "$gt": last_week}}).count()

    sc.rtm_send_message("general", "You've completed {0} pomodoros in the past \
        day, and {1} in the past week.".format(pomodoros_day, pomodoros_week))
