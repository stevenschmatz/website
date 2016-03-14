import datetime
import os
from flask import Flask, render_template
from app import db
from ava import launch_bot, sc
from api.pomodoro import bp as pomodoro_bp
from app.weather import get_weather_description

collection = db.shoutouts

app = Flask(__name__)


def register_all_blueprints():
    app.register_blueprint(pomodoro_bp)


@app.route("/")
def index():
    return render_template('landingPage.html')


@app.route("/weather")
def weather():
    return get_weather_description()


@app.route("/ava")
def ava():
    weather_description = get_weather_description()
    message = "Good morning! {0}".format(weather_description)
    sc.rtm_send_message("general", message)

    now = datetime.datetime.utcnow()
    yesterday = now - datetime.timedelta(days=1)
    last_week = now - datetime.timedelta(days=7)

    return db.pomodoro.find().count()

    # pomodoros_day = db.pomodoro.find({"time": {"$lt": now,
                                               # "$gt": yesterday}}).count()
    # pomodoros_week = db.pomodoro.find({"time": {"$lt": now,
                                                # "$gt": last_week}}).count()

    sc.rtm_send_message("general", "You've completed {0} pomodoros in the past \
        day, and {1} in the past week.".format(pomodoros_day, pomodoros_day))


if __name__ == "__main__":
    register_all_blueprints()
    port = int(os.environ.get("PORT", 5000))
    launch_bot()
    app.run(host='0.0.0.0', port=port, debug=True)
