pipi
====

shortcut install & freeze pip packages

.. image:: https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat
   :alt: contributions welcome
   :target: https://github.com/mehmetkose/pipi/

Usage
~~~~~

::

    pipi [package_name]
    pipi requests
    pipi pillow
    pipi rethinkdb

every single operation works like:

1. Create requirements.txt if not exists.
2. Try install the package if not installed.
3. Append to the requirements.txt if the operation is successful.

Installation
~~~~~~~~~~~~

::

    pip install pipi
