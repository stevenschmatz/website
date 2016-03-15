"""Database tools for modifying pomodoros."""

import datetime
from app import db


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
