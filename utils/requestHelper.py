from core.constants.constants import RESPONSE_NEW_LINE


class RequestHelper:
    @staticmethod
    def createHeader(key: str, value: str) -> str:
        return f'{key.capitalize()}: {value.lower()}{RESPONSE_NEW_LINE}'
