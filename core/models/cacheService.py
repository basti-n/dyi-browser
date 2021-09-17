from abc import abstractmethod, abstractproperty
from typing import Any


class CacheService:

    @abstractproperty
    def item(self) -> Any:
        pass

    @abstractmethod
    def shouldCache(self) -> bool:
        pass

    @abstractmethod
    def has(self) -> bool:
        pass

    @abstractmethod
    def get(self) -> Any:
        pass

    @abstractmethod
    def set(self) -> Any:
        pass
