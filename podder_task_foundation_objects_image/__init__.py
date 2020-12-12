__version__ = '0.1.0'

from .image import Image
from typing import Type
from podder_task_foundation.objects import LazyLoadFile


def get_class() -> Type[LazyLoadFile]:
    return Image
