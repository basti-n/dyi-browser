from typing import Any, Dict, List, Union
from core.constants.constants import CacheControlHeaders, HttpHeaders
from core.models.cacheService import CacheService
from utils.date import getCurrentUnixTime, httpDateToUnixTime
from itertools import chain

NO_CACHE_CONTROL_VALUES = [CacheControlHeaders.NO_CACHE.value,
                           CacheControlHeaders.NO_CACHE.value, CacheControlHeaders.REVALIDATE.value]


class RequestCacheService(CacheService):
    __cache = {}
    __cachable_http_statuscodes = (200, 301, 404)

    def __init__(self) -> None:
        super().__init__()

    def shouldCache(self, status: int, **headers) -> bool:
        if status not in self.__cachable_http_statuscodes:
            return False

        return not self.__includes(NO_CACHE_CONTROL_VALUES, **headers)

    def has(self, key: str) -> bool:
        if key in self.__cache:
            _, headers, __ = self.get(key)
            max_age_header = self.__get_cache_control_max_age(**headers)
            request_date = self.__get_cache_control_request_date(**headers)

            return not self.__cache_has_expired(max_age_header, request_date)

        return False

    def get(self, key: str) -> Any:
        return self.__cache[key]

    def set(self, key: str, value: Any) -> Any:
        return self.__add_to_cache(key, value)

    def __get_cache_control_header(self, **headers) -> Union[None, str]:
        return headers.get(HttpHeaders.CACHE_CONTROL.value)

    def __get_cache_control_header_values(self, **headers) -> Dict:
        cache_control_header = self.__get_cache_control_header(**headers)
        if cache_control_header:
            keyValuePairs = [cache_header.split(
                '=') for cache_header in cache_control_header.split(',')]

            cache_control_values = {}
            associated_key = None
            for value in chain(*keyValuePairs):
                if not associated_key:
                    associated_key = value
                    cache_control_values[value] = None
                else:
                    cache_control_values[associated_key] = value
                    associated_key = None

        return cache_control_values

    def __get_date_header(self, **headers) -> Union[None, str]:
        return headers.get(HttpHeaders.DATE.value)

    def __get_cache_control_max_age(self, **headers) -> Union[None, int]:
        return int(self.__get_cache_control_header_values(**headers)['max-age'])

    def __get_cache_control_request_date(self, **headers) -> Union[None, int]:
        date_header = self.__get_date_header(**headers)
        if date_header:
            return httpDateToUnixTime(date_header)

    def __add_to_cache(self, key: str, value: Any) -> Any:
        self.__cache[key] = value
        return self.get(key)

    def __includes(self, values: List[str], **headers) -> bool:
        cache_control_header = self.__get_cache_control_header(**headers)
        if not cache_control_header:
            return False

        return any([value.lower() in cache_control_header.lower() for value in values])

    def __cache_has_expired(self, request_date: int, max_age: int) -> bool:
        current_date = getCurrentUnixTime()
        return current_date - (request_date + max_age) < 0
