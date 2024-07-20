from api.utils import read_json


def test_lectura_json():
    assert read_json("not_exist_path.json") is None
