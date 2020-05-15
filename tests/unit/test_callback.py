import os

import pytest

from likemygf import callback

test_python_object = b"\x80\x03}q\x00X\x0e"
test_json_object = {"__class__": "bytes", "__value__": "gAN9"}


def test_to_json():
    encoded = callback.to_json(test_python_object)

    assert encoded


def test_to_json_raises():
    with pytest.raises(TypeError):
        encoded = callback.to_json("test")

        assert encoded


def test_from_json():
    decoded = callback.from_json(test_json_object)

    assert decoded


def test_onlogin_callback(tmpdir, mock_instagram_api_client):
    file = tmpdir.join("test.json")

    callback.onlogin(api=mock_instagram_api_client, new_settings_file=file)

    assert os.path.exists(file.strpath)
    assert os.path.isfile(file.strpath)
