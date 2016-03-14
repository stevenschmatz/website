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

    slack_token = os.environ.get('SLACK_TOKEN') or config['slack']['token']

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
