from apscheduler.schedulers.background import BackgroundScheduler
import pytz

sched = BackgroundScheduler(timezone=pytz.timezone('US/Eastern'))
