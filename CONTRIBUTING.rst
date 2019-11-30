Contributing
============

This contributing guide is trying to avoid common pitfalls, but the project
development environment is quite common. If it's not your first rodeo, here's a TL;DR

TL;DR
-----

(The following is not meant to be executed as a script)

.. code-block:: console

    $ # Install requirements
    $ pip install -r requirements.txt

    $ # Launch tests
    $ tox -e py37-tests

    $ # Use CLI
    $ weather Paris

Instructions for contribution
-----------------------------

Set up your development environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you plan to launch the project locally, install the package itself with development
dependencies in a virtual environment:

.. code-block:: console

    $ python3 -m venv venv
    $ source venv/bin/activate

You can check that your Python environment is properly activated:

.. code-block:: console

    (venv) $ which python
    /path/to/current/folder/venv/bin/python

Install local dependencies:

.. code-block:: console

    (venv) $ pip install -r requirements.txt

Run the project automated tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    (venv) $ tox -e py37-tests

Or

.. code-block:: console

    (venv) $ tox  # Run all the checks for all the interpreters

If you're not familiar with Pytest_, do yourself a treat and look into this fabulous
tool.

.. _Pytest: https://docs.pytest.org/en/latest/

If you don't know Tox_, have a look at their documentation, it's a very nice tool too.

.. _Tox: https://tox.readthedocs.io/en/latest/

To look at coverage in the browser after launching the tests, use:

.. code-block:: console

    $ python -m webbrowser htmlcov/index.html

Keep your code clean
^^^^^^^^^^^^^^^^^^^^

Before committing:

.. code-block:: console

    $ tox -e format

You can also install a `pre-commit`
hook which makes sure that all your commits are created clean:

.. code-block:: console

    cat > .git/hooks/pre-commit <<EOF
    #!/bin/bash -e
    exec ./pre-commit-hook
    EOF
    chmod +x .git/hooks/pre-commit

If ``tox`` is installed inside your ``virtualenv``, you may want to activate the
``virtualenv`` in ``.git/hooks/pre-commit``:

.. code-block:: bash

    #!/bin/bash -e
    source /path/to/venv/bin/activate
    exec ./pre-commit-hook

This will keep you from creating a commit if there's a linting problem.

Build the documentation
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ tox -e docs
    $ python -m webbrowser docs/_build/html/index.html
