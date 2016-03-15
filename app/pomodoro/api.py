"""Utilties to track work done."""

import json
import os
import datetime
from flask import Blueprint, request, redirect
from app import db, config
from db import work_summary

blueprint = Blueprint('pomodoro', __name__, url_prefix='/api')


@blueprint.route("/pomodoro", methods=['POST'])
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


@blueprint.route("/pomodoro", methods=['GET'])
def work_summary_json():
    """An API endpoint for getting pomodoro summaries."""
    return json.dumps(work_summary())
