
from rest_framework.renderers import JSONRenderer
from drf_json_keyformat import transformations

class CamelCaseJSONRenderer(JSONRenderer):
    """
    Renderer which serializes to JSON using camelCase keys.
    """
    def render(self, data, accepted_media_type=None, renderer_context=None):
        data = transformations.keys_to_camelcase(data)
        return super(CamelCaseJSONRenderer, self).render(data,
            accepted_media_type=accepted_media_type, renderer_context=renderer_context)


class PascalCaseJSONRenderer(JSONRenderer):
    """
    Renderer which serializes to JSON using PascalCase keys.
    """
    def render(self, data, accepted_media_type=None, renderer_context=None):
        data = transformations.keys_to_pascalcase(data)
        return super(PascalCaseJSONRenderer, self).render(data,
            accepted_media_type=accepted_media_type, renderer_context=renderer_context)
