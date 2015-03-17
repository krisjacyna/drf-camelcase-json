import json

from django.conf import settings
from rest_framework.parsers import JSONParser, ParseError, six
from drf_json_keyformat import transformations

class CamelCaseJSONParser(JSONParser):
    """
    Parses JSON-serialized data which has camelCase keys.
    """
    def parse(self, stream, media_type=None, parser_context=None):
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)
        try:
            data = stream.read().decode(encoding)
            return transformations.keys_to_snakecase(json.loads(data))
        except ValueError as exc:
            raise ParseError('JSON parse error - %s' % six.text_type(exc))


class PascalCaseJSONParser(JSONParser):
    """
    Parses JSON-serialized data which has PascalCase keys.
    """
    def parse(self, stream, media_type=None, parser_context=None):
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)
        try:
            data = stream.read().decode(encoding)
            return transformations.keys_to_snakecase(json.loads(data))
        except ValueError as exc:
            raise ParseError('JSON parse error - %s' % six.text_type(exc))
