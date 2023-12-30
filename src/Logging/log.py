import os
import typing
from datetime import date, time, datetime as dt
import time as tm
from typing import Any
import json
from loggers import *
import pandas as pd
from colorama import just_fix_windows_console
from settings import Settings, Standard
import utils

loggers = {}
just_fix_windows_console()


class Level:
    def __init__(self) -> None:
        pass

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

class Log(dict):
    def __init__(
        self,
        name,
        default_level: int,
        store: object = None,
        verbosity: bool = False,
        debug: bool = False,
        settings:Settings = Standard
    ) -> None:
        self.logs = []
        self._default_level = default_level
        self.verbosity = verbosity
        self._debug = debug
        self.store = store
        self.name = name
        self.settings = settings

    def log(self, level, notes):
        def log_decorater(func):
            def log_wrapper(*args, **kwargs):
                log = Event_Log(level=level, notes=notes, func=func)
                self.add_log(log)
                func(*args, **kwargs)
                return func

            return log_wrapper

        return log_decorater

    def add_log(self, Log):
        colours = self.settings.colours
        Log.level = self.levels[Log.level_num]
        Log.list.insert(2, Log.level)
        Log.NCList.insert(2, Log.level)
        if str(Log.level) != "Debug":
            if int(Log.level_num) > 2:
                if self.verbosity == True:
                    print(
                        f"====== LOGGER ======\n\nEvent\n    {colours[Log.level_num]["level"]["fore"]}Level: {Log.level}\n    Function: {Log.func}\n    Notes: {Log.notes}\n    Time: {Log.time}\n    Date: {Log.date}"
                    )
                else:
                    print(f"{Log.time} {Log.level}:{self.name}    {Log.notes}")
            self.logs.append(Log)
        else:
            if self._debug:
                if self.verbosity == True:
                    print(f"====== DEBUG ======\n\nDebug\n    ULID: {Log.ULID}\n    Function:{Log.function}\n    Notes: {Log.notes}\n    Time: {Log.time}\n    Date: {Log.date}")

    def print(self):
        data = []
        for log in self.logs:
            data.append(log.NCList)

        self.data = pd.DataFrame(data, columns = ["Date", "Time", "Level name", "Level", "Notes", "Func"])
        print(self.data)

    def dict(self, filter: typing.Union[None, list] = None):
        _dict = []
        for log in self.logs:
            x = {
                "Level": log.level,
                "Notes": log.notes,
                "Function": log.func,
                "Datetime": {"Time": log.time, "Date": log.date},
            }
            _dict.append(x)
        return _dict




class master:

    @classmethod
    def new(
        cls,
        logger,
        default_level: int,
        store: object = None,
        verbosity: bool = False,
        debug: bool = False,
        settings:typing.Union[Settings, str, ] = Standard
    ) -> Log:
        log = Log(
            default_level=default_level, store=store, settings=settings, verbosity=verbosity, debug=debug, name=logger
        )
        loggers[logger] = log
        return log

    @classmethod
    def get_logggers(cls):
        return loggers
    
    @classmethod
    def new_level(cls, levels:typing.Union[int, list[int]], loggers:typing.Union[Log, list[Log]], names:typing.Union[str, list[str]]):
        if isinstance(loggers, list):
            for i in range(len(levels)):
                master.new_level(levels[i], loggers[i], names[i])
        elif isinstance(loggers, Log):
            logger = loggers
            level:int=levels
            name:str = name 
            logger.levels[level] = name


    
    @classmethod
    def remove_level(cls, levels:typing.Union[int, list[int]], loggers:typing.Union[Log, list[Log]]):
        if isinstance(loggers, list):
            for i in range(len(levels)):
                master.remove_level(levels[i], loggers[i])
        elif isinstance(loggers, Log):
            logger = loggers
            level:int=levels
            logger.levels.remove(level)