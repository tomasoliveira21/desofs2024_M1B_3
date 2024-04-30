from apscheduler.schedulers.blocking import BlockingScheduler
import pytz

from socialNet_backend import app
from socialNet_backend.lib.logger import get_logger
from socialNet_backend.tasks import heartbeat


app.initialize()
logger = get_logger(__name__)

pacific_timezone = pytz.timezone('US/Pacific')


scheduler = BlockingScheduler(timezone=pacific_timezone)


@scheduler.scheduled_job('cron', minute='*')
def cron_heartbeat_task():
    logger.info('Launching heartbeat task')
    heartbeat.delay()


def run():
    logger.info("Starting scheduler")
    scheduler.start()
