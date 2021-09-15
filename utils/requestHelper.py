from core.constants.constants import RESPONSE_NEW_LINE


class RequestHelper:
    @staticmethod
    def createHeader(key: str, value: str) -> str:
        return f'{key[:1].upper() + key[1:]}: {value.lower()}{RESPONSE_NEW_LINE}'
