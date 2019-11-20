import click

from .api_connector import fetch_api, get_city_id, parse_forecasts
from .exceptions import NetworkError, UnknownCityError


@click.command(name="weather")
@click.argument("name")
def cli(name) -> None:
    try:
        city_id = get_city_id(name)
        forecasts = fetch_api(city_id)
    except UnknownCityError:
        raise click.UsageError(f"Unknown city {name}.")
    except NetworkError:
        raise click.UsageError("Network error, please retry later.")
    else:
        if parse_forecasts(forecasts):
            click.echo(f"It is going to rain today in {name}.")
        else:
            click.echo(f"It is not going to rain today in {name}.")


def main():
    return cli()
