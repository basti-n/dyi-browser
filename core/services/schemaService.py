from utils.url import getSchema, stripSchema


class SchemaService:
    def __init__(self, host: str) -> None:
        self._host = host

    @property
    def schema(self) -> str:
        return getSchema(self._host)

    @property
    def schemalessPath(self) -> str:
        return stripSchema(self._host)

    @property
    def host(self) -> str:
        return self.schemalessPath.split('/')[0]
