from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler({
    'apscheduler.timezone': 'UTC'
})
