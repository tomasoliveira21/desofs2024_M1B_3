from socialnet.lib.dates import utcnow

from socialNet_backend.lib.celery import task
from socialNet_backend.lib.logger import get_logger


logger = get_logger(__name__)


@task
def heartbeat():
    logger.info('Heartbeat %s', utcnow())
