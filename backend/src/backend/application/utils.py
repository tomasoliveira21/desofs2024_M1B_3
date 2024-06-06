from contextlib import contextmanager
from typing import Any


@contextmanager
def single_read_object(object: Any):
    try:
        yield object
    finally:
        del object
