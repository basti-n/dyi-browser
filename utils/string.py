import re


def camelCaseToKebabCase(camelCased: str) -> str:
    """ Converts the provided string into kebab case ('-') """
    return re.sub("([A-Z])", "-\\1", camelCased).lower().lstrip("-")
