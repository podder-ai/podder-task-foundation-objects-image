from pathlib import Path
from typing import Optional, Tuple, Union

import numpy
from PIL import Image as PILImage
from PIL import ImageOps
from podder_task_foundation.objects import LazyLoadFile


class Image(LazyLoadFile):
    supported_extensions = [
        ".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".tif", ".tiff"
    ]
    type = "image"
    default_extension = ".png"

    def __init__(self,
                 data: Optional[Union[PILImage.Image, numpy.ndarray,
                                      numpy.generic]] = None,
                 path: Optional[Path] = None,
                 name: Optional[str] = None,
                 *args):
        raw_data = None
        if data is not None:
            if isinstance(data, PILImage.Image):
                raw_data = ImageOps.exif_transpose(data)
            elif isinstance(data, (numpy.ndarray, numpy.generic)):
                raw_data = PILImage.fromarray(data)

        super().__init__(raw_data, path, name)

    def __repr__(self):
        return self.to_repr()

    def __str__(self):
        return self.to_str()

    def to_dict(self) -> dict:
        size = self.get_size()
        if size is None:
            return {}
        width, height = size
        return {
            "width": width,
            "height": height,
        }

    def to_repr(self) -> str:
        return "<Type: {} Format:{} Size:{} Mode:{}>".format(
            self.type, self.data.format, self.data.size, self.data.mode)

    def to_str(self) -> str:
        return "<Type: {} Format:{} Size:{} Mode:{}>".format(
            self.type, self.data.format, self.data.size, self.data.mode)

    def _lazy_load(self):
        raw_data = PILImage.open(str(self._path))
        self._data = ImageOps.exif_transpose(raw_data)

    def save(self,
             path: Path,
             encoding: Optional[str] = 'utf-8',
             indent: Optional[int] = None,
             *args) -> bool:

        if path.suffix == ".jpg" or path.suffix == ".jpeg":
            self.data.save(str(path), quality=90)
        else:
            self.data.save(str(path))

        return True

    def get(self,
            data_format: Optional[str] = None,
            *args) -> Optional[object]:
        if data_format == "numpy" or data_format == "opencv":
            return numpy.array(self._data)
        return self._data

    def get_size(self) -> Optional[Tuple]:
        image = self.data
        if image is None:
            return None

        return image.size
