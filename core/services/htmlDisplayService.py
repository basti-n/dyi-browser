from core.models.displayService import DisplayService
from enum import Enum


class HtmlBrackets(Enum):
    OPEN_TAG = '<'
    CLOSE_TAG = '>'


class HTMLDisplayService(DisplayService):
    def __init__(self, body: str) -> None:
        super().__init__()
        self.body = body

    def show(self) -> str:
        in_angle = False

        for char in self.body:
            if char == HtmlBrackets.OPEN_TAG.value:
                in_angle = True

            if not in_angle:
                print(char, end='')

            if char == HtmlBrackets.CLOSE_TAG.value:
                in_angle = False

        print('')
