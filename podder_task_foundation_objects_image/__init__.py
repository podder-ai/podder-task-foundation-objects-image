__version__ = '0.1.2'

from typing import Type

from .image import Image


def get_class() -> Type[Image]:
    return Image
