from abc import abstractmethod


class DisplayService:

    @abstractmethod
    def show() -> str:
        pass
