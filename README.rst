Django Client Data
==================

This allows Django to pass data to the browser.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django_client_data

Add ``django_client_data`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'django_client_data',
    )

Install middleware.

Install context processor.

Usage
-----

Call ``set_client_data()``.

Include ``client_data.html`` in your page.

Settings
--------

CLIENT_DATA_NAMESPACE, defaults to 'DJANGO', the data is a property of this name
named 'client_data'.

Mechanism
---------

Django Client Data works by attaching a ``client_data`` attribute on the request
object.  The ``client_data.html`` template attaches a ... to the JavaScript
global indicated by CLIENT_DATA_NAMESPACE.

Todo
----

* add a "context processors" feature to client data so custom values can be
injected

Run Tests
---------

.. code-block:: bash

    ./configure.sh
    source venv/bin/activate
    python manage.py test