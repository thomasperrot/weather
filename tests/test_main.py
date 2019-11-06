import os
import json

import pytest

from main import parse_forecasts


@pytest.mark.parametrize(
    "file_name, expected_result",
    [
        pytest.param("full_rainy_response.json", True, id="Full rainy response"),
        pytest.param("full_sunny_response.json", False, id="Full sunny response"),
        pytest.param("mixed_response.json", True, id="Mixed response"),
    ]
)
def test_parse_forecasts(file_name: str, expected_result: bool) -> None:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, file_name)) as f:
        api_response = json.load(f)
        assert parse_forecasts(api_response) is expected_result
