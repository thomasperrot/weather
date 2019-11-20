import pytest
from click.testing import CliRunner

from weather import cli, exceptions


def test_cli_unknown_city(monkeypatch):
    def mock_get_city_id(_):
        raise exceptions.UnknownCityError

    monkeypatch.setattr(cli, "get_city_id", mock_get_city_id)
    result = CliRunner().invoke(cli.cli, ["unknown"])
    assert result.exit_code == 2
    assert (
        result.output == "Usage: weather [OPTIONS] NAME\n\n"
        "Error: Unknown city unknown.\n"
    )


def test_cli_network_error(monkeypatch):
    def mock_get_city_id(_):
        raise exceptions.NetworkError

    monkeypatch.setattr(cli, "get_city_id", mock_get_city_id)
    result = CliRunner().invoke(cli.cli, ["Paris"])
    assert result.exit_code == 2
    assert (
        result.output == "Usage: weather [OPTIONS] NAME\n\n"
        "Error: Network error, please retry later.\n"
    )


@pytest.mark.parametrize(
    "forecasts_result, outpout",
    [
        pytest.param(True, "It is going to rain today in Paris.\n", id="Raining"),
        pytest.param(
            False, "It is not going to rain today in Paris.\n", id="Not raining"
        ),
    ],
)
def test_cli_there_is_rain(monkeypatch, forecasts_result, outpout):
    def mock_get_city_id(_):
        return 1

    def mock_fetch_api(_):
        return {}

    def mock_parse_forecasts(_):
        return forecasts_result

    monkeypatch.setattr(cli, "get_city_id", mock_get_city_id)
    monkeypatch.setattr(cli, "fetch_api", mock_fetch_api)
    monkeypatch.setattr(cli, "parse_forecasts", mock_parse_forecasts)
    result = CliRunner().invoke(cli.cli, ["Paris"])
    assert result.exit_code == 0
    assert result.output == outpout
