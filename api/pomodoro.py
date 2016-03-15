"""Utilties to track work done."""

import json
import os
import datetime
from flask import Blueprint, request, redirect
from app import db, config

bp = Blueprint('pomodoro', __name__, url_prefix='/api')


@bp.route("/pomodoro", methods=['POST'])
def log_pomodoro():
    """Logs a Pomodoro to the 'pomodoro' db collection.

    Accessible through the /pomodoro Slack command.
    """

    if config is not None:
        slack_token = config['slack']['pomodoro_token']
    else:
        slack_token = os.environ.get('SLACK_TOKEN')

    # Return forbidden error if token is incorrect
    if slack_token != request.form['token']:
        return redirect('/'), 403

    # Insert the pomodoro
    pomodoro = {
        "text": request.form['text'],
        "time": datetime.datetime.utcnow()
    }
    db.pomodoro.insert(pomodoro)

    response = "Pomodoro logged successfully: '%s'." % request.form['text']

    return response, 200


def work_summary():
    """Returns a summary of pomodoros done in the past 24 hours and
    past week."""

    now = datetime.datetime.utcnow()
    yesterday = now - datetime.timedelta(days=1)
    last_week = now - datetime.timedelta(days=7)

    pomodoros_day = db.pomodoro.find({"time": {"$lt": now,
                                               "$gt": yesterday}}).count()
    pomodoros_week = db.pomodoro.find({"time": {"$lt": now,
                                                "$gt": last_week}}).count()
    return {
        "day": pomodoros_day,
        "week": pomodoros_week
    }


@bp.route("/pomodoro", methods=['GET'])
def work_summary_json():
    """An API endpoint for getting pomodoro summaries."""
    return json.dumps(work_summary())


def work_summary_english():
    """A natural language description of work done."""
    pomodoros = work_summary()
    return ("You've completed {0} pomodoros in the past day, "
            "and {1} in the past week.").format(pomodoros["day"],
                                                pomodoros["week"])
