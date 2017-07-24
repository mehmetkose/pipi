pipi
====

.. image:: https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat
   :alt: contributions welcome
   :target: https://github.com/mehmetkose/pipi/

shortcut install & freeze pip packages

Installation
~~~~~~~~~~~~

::

  pip install pipi


Usage
~~~~~

::

    pipi install [package_name]
    pipi i [package_name]
    pipi install requests
    pipi i requests

every single operation works like:

1. Create requirements.txt if not exists.
2. Try install the package if not installed.
3. Append package to the requirements.txt if the operation is successful.
