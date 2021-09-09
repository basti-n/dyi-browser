class FileService:
    @staticmethod
    def readFile(path: str) -> None:
        with open(path, encoding='utf8') as f:
            print(f.read())
