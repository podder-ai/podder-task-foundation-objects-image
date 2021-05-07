from pathlib import Path

from podder_task_foundation_objects_image import Image


def test_image_create():
    path = Path(__file__).parent.parent.joinpath("data", "image_01.png")
    _object = Image(path=path)
    assert _object.type == "image"

    file_name = _object.get_file_name()
    assert file_name.name == "image_01.png"
