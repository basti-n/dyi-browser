from utils.url import getSchema, stripSchema


class SchemaService:
    def __init__(self, host: str) -> None:
        self.host = host

    @property
    def schema(self) -> str:
        return getSchema(self.host)

    @property
    def schemalessPath(self) -> str:
        return stripSchema(self.host)
