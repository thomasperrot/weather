from typing import Dict

import requests

from .exceptions import NetworkError, UnknownCityError

RAINY_STATES = ["hr", "lr", "s"]


def fetch_city_id(city_name: str) -> int:
    try:
        r = requests.get(
            url="https://www.metaweather.com/api/location/search/",
            params={"query": city_name},
        )
        r.raise_for_status()
    except requests.RequestException:
        raise NetworkError
    if not r.json():
        raise UnknownCityError
    return r.json()[0]["woeid"]


def fetch_forecasts(city_id: int) -> Dict:
    try:
        r = requests.get(url=f"https://www.metaweather.com/api/location/{city_id}")
    except requests.RequestException:
        raise NetworkError
    if not r.json():
        raise UnknownCityError
    return r.json()


def parse_forecasts(forecasts: Dict) -> bool:
    """Return True if more than half of the forecasts announce rain, False otherwise."""

    rainy_forecasts = sum(
        1
        for f in forecasts["consolidated_weather"]
        if f["weather_state_abbr"] in RAINY_STATES
    )
    return rainy_forecasts >= len(forecasts["consolidated_weather"]) / 2
