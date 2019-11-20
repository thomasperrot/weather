from unittest.mock import MagicMock

import pytest

from weather import __main__


@pytest.mark.parametrize("name, called", [("something", False), ("__main__", True)])
def test_main(monkeypatch, name, called):
    mock_cli = MagicMock()
    monkeypatch.setattr(__main__.cli, "cli", mock_cli)
    __main__.main(name)
    assert mock_cli.called is called
