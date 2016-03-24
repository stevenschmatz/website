from app.scheduler import sched
from . import send_me
from random import choice


def daily_summary():
    greeting = choice([
        "Good morning, Steven!",
        "Hi, Steven!",
        "Hey there, Steven!",
        "Good morning!"
    ])

    filler = choice([
        "Today, focus on improving",
        "Your theme to think about today is",
        "Today, try to cultivate"
    ])

    theme = choice([
        "authenticity: let go of what people think about you",
        "self-compassion: let go of perfectionism",
        "resiliency: let go of numbing and powerlessness",
        "gratitude and joy: let go of scarcity",
        "intuition and faith: let go of the need for certainty",
        "creativity: let go of comparison",
        ("play and rest: let go of exhaustion as a status symbol and "
            "productivity as self-worth"),
        "calm and stillness: let go of anxiety as a lifestyle",
        "meaningful work: let go of self-doubt and 'supposed to'",
        ("laughter, song, and dance: let go of being cool and 'always in "
            "control'")
    ])

    message = "{0} {1} {2}.".format(greeting, filler, theme)

    send_me(message)


def add_cron_jobs():
    sched.add_job(daily_summary, "cron", hour=13, minute=54)
