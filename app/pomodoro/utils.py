from db import work_summary


def work_summary_english():
    """A natural language description of work done."""
    pomodoros = work_summary()
    return ("You've completed {0} pomodoros in the past day, "
            "and {1} in the past week.").format(pomodoros["day"],
                                                pomodoros["week"])
