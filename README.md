# Weather

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.6](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Build Status](https://travis-ci.com/thomasperrot/weather.svg?branch=master)](https://travis-ci.org/thomasperrot/weather)
[![codecov](https://codecov.io/gh/thomasperrot/weather/branch/master/graph/badge.svg)](https://codecov.io/gh/thomasperrot/weather)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A simple CLI to know whether or not it is going to rain today.

## Usage

```
$ python main.py NAME
```

Example

```
$ python main.py Paris
It is going to rain today in Paris.
```

## Installation

```
$ pip3 install requirements/local.txt
```

## Tests

```
$ pip3 install requirements/test.txt
$ py.test -v
```

## Improvments

- Add options to select the desired weather besides of rain
- Find a better name for this app
