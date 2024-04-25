from socialNet_backend.service.user.creation import create_user
from socialNet_backend.utils.string import random_string


def make_user(email=None, password='alvintester', **fields):
    email = email or '{}@socialnet.com'.format(random_string(12))
    user = create_user(email, password, email_verified=True, **fields)
    return user
