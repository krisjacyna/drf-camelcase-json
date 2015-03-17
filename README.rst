=====
JSON Key Formats
=====
A plugin app for `Django REST Framework`_.

This provides renderers and parsers to transform python style snake_case keys to and from different formats. 
Currently supporting camelCase or PascalCase.

.. image:: https://travis-ci.org/krisjacyna/drf-json-keyformat.svg?branch=master
    :target: https://travis-ci.org/krisjacyna/drf-json-keyformat

=====
Installation
=====

1. Clone or download this project
2. ``cd`` into the directory and install with::

    $ python setup.py install
3. Add the renderers/parsers to your Django app::

    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': (
            'drf_json_keyformat.renderers.CamelCaseJSONRenderer',
            # other renderers
        ),
        'DEFAULT_PARSER_CLASSES': (
            'drf_json_keyformat.parsers.CamelCaseJSONParser',
            # other parsers
        )
    }
    
Refer to the `DRF documentation`_ about including custom renders.

=====
Unit Tests
=====
To run the unit tests, run the following:
::
    $ python -m unittest discover


.. _`Django REST Framework`: http://www.djangorestframework.com
.. _`DRF documentation`: http://www.django-rest-framework.org/api-guide/renderers/
