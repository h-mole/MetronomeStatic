from PyBirdViewCode.utils import file_to_dataurl, parse_dataurl
from tests.base import asset_path


def test_file_data_url():
    png_path = asset_path("./files/icon.png")
    with open(png_path, "rb") as f:
        original = f.read()
    url = file_to_dataurl(png_path)
    mime, parsed = parse_dataurl(url)
    assert mime == "image/png"
    assert parsed == original
