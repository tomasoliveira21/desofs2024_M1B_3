#!/usr/bin/env python

from socialNet_backend import app
from socialNet_backend.app import config  # noqa
from socialNet_backend.db import get_session
from socialNet_backend.db.models import *  # noqa
from socialNet_backend.lib.logger import get_logger
from socialNet_backend.lib.redis import get_redis_connection   # noqa

app.initialize()

logger = get_logger()
session = get_session()
