import json
import os

import pytest
import requests

from weather import api_connector, exceptions


def test_get_city_id_unknown_city(monkeypatch):
    class MockResponse:
        def json(self):
            return []

    class MockRequest:
        @staticmethod
        def get(*args, **kwargs):
            return MockResponse()

    monkeypatch.setattr(api_connector, "requests", MockRequest)
    with pytest.raises(exceptions.UnknownCityError):
        api_connector.get_city_id("unknown")


def test_get_city_id_request_error(monkeypatch):
    class MockRequest:
        RequestException = requests.RequestException

        @staticmethod
        def get(*args, **kwargs):
            raise requests.RequestException

    monkeypatch.setattr(api_connector, "requests", MockRequest)
    with pytest.raises(exceptions.NetworkError):
        api_connector.get_city_id("unknown")


def test_get_city_id_request(monkeypatch):
    class MockResponse:
        def json(self):
            return [
                {
                    "title": "Paris",
                    "location_type": "City",
                    "woeid": 615702,
                    "latt_long": "48.856930,2.341200",
                }
            ]

    class MockRequest:
        @staticmethod
        def get(*args, **kwargs):
            return MockResponse()

    monkeypatch.setattr(api_connector, "requests", MockRequest)
    response = api_connector.get_city_id("Paris")
    assert response == 615702


def test_fetch_api_unknown_city(monkeypatch):
    class MockResponse:
        def json(self):
            return []

    class MockRequest:
        @staticmethod
        def get(*args, **kwargs):
            return MockResponse()

    monkeypatch.setattr(api_connector, "requests", MockRequest)
    with pytest.raises(exceptions.UnknownCityError):
        api_connector.fetch_api(1)


def test_fetch_api_request_error(monkeypatch):
    class MockRequest:
        RequestException = requests.RequestException

        @staticmethod
        def get(*args, **kwargs):
            raise requests.RequestException

    monkeypatch.setattr(api_connector, "requests", MockRequest)
    with pytest.raises(exceptions.NetworkError):
        api_connector.fetch_api(1)


def test_fetch_api_request(monkeypatch):
    class MockResponse:
        def json(self):
            return [{"city": "Paris"}]

    class MockRequest:
        @staticmethod
        def get(*args, **kwargs):
            return MockResponse()

    monkeypatch.setattr(api_connector, "requests", MockRequest)
    response = api_connector.fetch_api(1)
    assert response == [{"city": "Paris"}]


@pytest.mark.parametrize(
    "file_name, expected_result",
    [
        pytest.param("full_rainy_response.json", True, id="Full rainy response"),
        pytest.param("full_sunny_response.json", False, id="Full sunny response"),
        pytest.param("mixed_response.json", True, id="Mixed response"),
    ],
)
def test_parse_forecasts(file_name: str, expected_result: bool):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "fixtures", file_name)) as f:
        api_response = json.load(f)
        assert api_connector.parse_forecasts(api_response) is expected_result
