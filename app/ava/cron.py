from app.scheduler import sched
from . import send_me


def hello_world():
    send_me("Hello, world!")


def add_cron_jobs():
    sched.add_job(hello_world, "cron", hour=19, minute=41)
