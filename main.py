from typing import Dict

import requests
import click


RAINY_STATES = ["hr", "lr", "s"]


class UnknownCityError(ValueError):
    pass


@click.command(name="check-raining")
@click.argument("name")
def main(name) -> None:
    try:
        city_id = get_city_id(name)
        forecasts = fetch_api(city_id)
    except UnknownCityError:
        click.echo(f"Unknown city: {name}.")
    except requests.RequestException:
        click.echo("Network error, please retry later.")
    else:
        if parse_forecasts(forecasts):
            click.echo(f"It is going to rain today in {name}.")
        else:
            click.echo(f"It is not going to rain today in {name}.")


def get_city_id(city_name: str) -> int:
    r = requests.get(
        url="https://www.metaweather.com/api/location/search/",
        params={"query": city_name},
    )
    if not r.json():
        raise UnknownCityError
    return r.json()[0]["woeid"]


def fetch_api(city_id: int) -> Dict:
    r = requests.get(url=f"https://www.metaweather.com/api/location/{city_id}")
    if not r.json():
        raise UnknownCityError
    return r.json()


def parse_forecasts(forecasts: Dict) -> bool:
    """Return True if more than half of the forecasts announce rain, False otherwise."""

    rainy_forecasts = sum(1 for f in forecasts["consolidated_weather"] if f["weather_state_abbr"] in RAINY_STATES)
    return rainy_forecasts >= len(forecasts["consolidated_weather"]) / 2


if __name__ == '__main__':
    main()
