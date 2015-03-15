import re

def _underscore_repl(match):
    return match.group()[1].upper()


def str_to_camelcase(str_value):
    """
    Transforms a snake case string value to camelcase, where underscores are
    removed and characters immediately following the underscore are capitalized.

    The first charater will become lowercase if not already.
    """
    camel = re.sub(r'_[a-zA-Z]', _underscore_repl, str_value)
    # downcase first letter in case it was uppercase
    camel = camel[0].lower() + camel[1:]
    return camel


def str_to_pascalcase(str_value):
    """
    Transforms a snake case string value to pascalcase, where underscores are
    removed and characters immediately following the underscore are capitalized.

    The first charater will become uppercase if not already.
    """
    pascal = re.sub(r'_[a-zA-Z]', _underscore_repl, str_value)
    # upcase first letter in case it was lowercase
    pascal = pascal[0].upper() + pascal[1:]
    return pascal


def _transform_keys(data, key_transformer):
    if isinstance(data, dict):
        transformed = {}
        for key, value in data.items():
            camel_key = key_transformer(key)
            transformed[camel_key] = _transform_keys(value, key_transformer)
        return transformed

    if isinstance(data, (list, tuple)):
        for i in range(len(data)):
            data[i] = _transform_keys(data[i], key_transformer)
        return data
    return data


def keys_to_camelcase(data):
    """
    Returns a recursively transformed copy of a string keyed dict
    where the keys are replaced with camel case equivalents.
    """
    return _transform_keys(data, str_to_camelcase)


def keys_to_pascalcase(data):
    """
    Returns a recursively transformed copy of a string keyed dict
    where the keys are replaced with pascal case equivalents.
    """
    return _transform_keys(data, str_to_pascalcase)
