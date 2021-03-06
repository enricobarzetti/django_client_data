Django Client Data
==================

This allows Django to export JSON-compatible data to the browser.  The
client-side code accesses the data as a JavaScript object.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django_client_data

Install the app, middleware, and context processor

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'django_client_data',
    )

    MIDDLEWARE_CLASSES = (
        ...
        'django_client_data.middleware.ClientDataMiddleware',
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        'django_client_data.context_processors.client_data',
    )

Usage
-----

Call ``set_client_data()`` in your view to export values

.. code-block:: python

    from django.views.generic import TemplateView
    from django_client_data import set_client_data


    class IndexView(TemplateView):
        template_name = 'index.html'

        def get(self, request, *args, **kwargs):
            set_client_data(request, **{'foo': 'bar'})
            return super(IndexView, self).get(request, *args, **kwargs)

Include ``client_data.html`` in your page

.. code-block:: django

    {% include 'django_client_data/client_data.html' %}

The JavaScript object ``DJANGO.client_data`` will look like

.. code-block:: javascript

    {
        "DEBUG": false,
        "STATIC_URL": "/static/",
        "csrftoken": "gSlpOPyxHrdQH3KWUEkXx1wfyqGE7MDo",
        "foo": "bar",
        "url_args": [],
        "url_kwargs": {},
        "url_name": "index",
        "user_full_name": null,
        "user_pk": null,
        "username": null
    }

Settings
--------

CLIENT_DATA_NAMESPACE (defaults to 'DJANGO') is the JavaScript global that will
be created as the namespace to contain the client data.  The data is a property
of this global and is named 'client_data'.

Mechanism
---------

Django Client Data works by attaching a ``client_data`` attribute on the request
object.  The ``client_data.html`` template attaches a ``client_data`` property
to the JavaScript global indicated by CLIENT_DATA_NAMESPACE.

Todo
----

* Add a "context processors" feature to client data so custom values can be
  injected

Run Tests
---------

.. code-block:: bash

    ./configure.sh
    source venv/bin/activate
    python django_client_data/tests/manage.py test
