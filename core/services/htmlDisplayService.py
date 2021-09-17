from typing import List
from core.models.displayService import DisplayService
from enum import Enum
from xml.sax import saxutils as su
import re


class HtmlBrackets(Enum):
    OPEN_TAG = '<'
    CLOSE_TAG = '>'


class HTMLDisplayService(DisplayService):
    def __init__(self, body: str) -> None:
        super().__init__()
        self.body = body

    def show(self, *, body=None, view_source=False) -> str:
        if view_source:
            print('***' * 3, 'VIEW-SOURCE', '***' * 3)
            print(body or self.body)
            print('***' * 9)

        content = self.__strip_tags(body or self.body)

        print(content)
        print('')

    def findAllBetweenTag(self, html: str, tag: str) -> List[str]:
        """ Returns a list of all content found within the tags """
        match = re.findall(rf'(?<=<{tag}>)(.*?)(?=<\/{tag}>)',
                           html, flags=re.MULTILINE | re.DOTALL)

        return match

    def __unescape(self, content: str) -> str:
        return su.unescape(content)

    def __strip_tags(self, content: str, *, debug=False) -> str:
        """ Removes all tags from provided content strings """
        in_angle = False
        stripped_content = ''

        for char in content:
            if char == HtmlBrackets.OPEN_TAG.value:
                in_angle = True

            if not in_angle:
                unescaped_char = self.__unescape(char)
                if debug:
                    print(unescaped_char, end='')

                stripped_content = stripped_content + unescaped_char

            if char == HtmlBrackets.CLOSE_TAG.value:
                in_angle = False

        return stripped_content
