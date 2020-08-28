*******
Weather
*******

.. image:: https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue?logo=python&logoColor=white
   :target: https://www.python.org/downloads/release
   :alt: Python3.6+ compatible

.. image:: https://img.shields.io/readthedocs/get-weather?logo=read-the-docs
    :target: http://get-weather.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/github/workflow/status/thomasperrot/weather/CI?logo=github
   :target: https://github.com/thomasperrot/weather/actions?workflow=tests
   :alt: Continuous Integration Status

.. image:: https://codecov.io/gh/thomasperrot/weather/branch/master/graph/badge.svg?logo=codecov
   :target: https://codecov.io/gh/thomasperrot/weather
   :alt: Coverage Status

.. image:: https://img.shields.io/badge/License-MIT-green.svg
   :target: https://github.com/thomasperrot/weather/blob/master/LICENSE.rst
   :alt: MIT License

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style black

A simple CLI to know whether it is going to rain today in a given city, using MetaWeather_ API_.

.. _MetaWeather: https://www.metaweather.com/
.. _API: https://www.metaweather.com/api/

Here's an example

.. code-block:: bash

   weather Paris
   It is going to rain today in Paris.

Quickstart
**********

.. code-block:: bash

   python setup.py install

Improvments
***********

- Add options (verbosity, etc.)
- Upload as pypi package
- Find a better name for this app

.. Below this line is content specific to the README that will not appear in the doc.
.. end-of-index-doc

Where to go from here
---------------------

The complete docs_ is probably the best place to learn about the project.

If you encounter a bug, or want to get in touch, you're always welcome to open a
ticket_.

.. _docs: http://get-weather.readthedocs.io/en/latest
.. _ticket: https://github.com/thomasperrot/weather/issues/new
