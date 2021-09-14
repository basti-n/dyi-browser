from core.models.displayService import DisplayService
from enum import Enum
import re


class HtmlBrackets(Enum):
    OPEN_TAG = '<'
    CLOSE_TAG = '>'


class HTMLDisplayService(DisplayService):
    def __init__(self, body: str) -> None:
        super().__init__()
        self.body = body

    def show(self, *, body=None) -> str:
        in_angle = False

        for char in body or self.body:
            if char == HtmlBrackets.OPEN_TAG.value:
                in_angle = True

            if not in_angle:
                print(char, end='')

            if char == HtmlBrackets.CLOSE_TAG.value:
                in_angle = False

        print('')

    def findAllBetweenTag(self, html: str, tag: str) -> list[str]:
        """ Returns a list of all content found within the tags """
        match = re.findall(rf'(?<=<{tag}>)(.*?)(?=<\/{tag}>)',
                           html, flags=re.MULTILINE | re.DOTALL)

        return match
