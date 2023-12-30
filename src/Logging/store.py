import typing
import requests
#import pydir
import enum


class Info:
    def __init__(self, time, level, logger, notes, date, func=None) -> None:
        self.time = time
        self.logger = logger
        self.notes = notes
        self.date = date
        self.func = func
        self.level = level


class File:
    def __init__(self, file: str, file_mode: str) -> None:
        self.file = file
        self.file_mode = file_mode

    def __call__(self, info: Info) -> typing.Any:
        with open(self.file, self.file_mode) as f:
            f.write(f"{info.time} | {info.logger} {info.level}: {info.notes}")


class Https(enum.Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"

    def __init__(
        self, url: str, mode: typing.Union[GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS]
    ):
        self.url = url
        self.type = type
        self.mode = mode.lower()
        print(f"Logger: Sending debug infomation to {self.url}")

    def __call__(self, info: dict) -> typing.Any:
        mode = self.mode
        method = mode.upper()
        if method == "GET":
            response = requests.get(self.url)
        elif method == "POST":
            response = requests.post(self.url, data=info)
        elif method == "PUT":
            response = requests.put(self.url, data=info)
        elif method == "DELETE":
            response = requests.delete(self.url)
        elif method == "PATCH":
            response = requests.patch(self.url, data=info)
        elif method == "HEAD":
            response = requests.head(self.url)
        elif method == "OPTIONS":
            response = requests.options(self.url)
