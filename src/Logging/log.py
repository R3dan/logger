import os
import typing
from datetime import date, time, datetime as dt
import time as tm
from typing import Any
import json
from loggers import *



loggers = {}



class Log():

    def __init__(self, name, default_level:int, store:object=None, verbosity:bool = False, debug:bool = False) -> None:
        self.logs = []
        self._default_level = default_level
        self.verbosity = verbosity
        self._debug = debug
        self.store = store
        self.name = name


    
    def log(self, level, notes):
        def log_decorater(func):
            def log_wrapper(*args, **kwargs):
                log=Event_Log(level=level, notes=notes, func=func)
                self.add_log(log)
                func(*args, **kwargs)
                return func
            return log_wrapper
        return log_decorater
    

    
    
    def add_log(self, Log):
        if int(Log.level) > 2:
            if self.verbosity == True:
                print(f"====== DEBUGGER ======\n\nEvent\n    Level: {Log.level}\n    Function: {Log.func}\n    Notes: {Log.notes}\n    Time: {Log.time}\n    Date: {Log.date}")
            else:
                print(f"{Log.time} {Log.level}:{self.name}    {Log.notes}")
        self.logs.append(Log)

    def print(self):
        for log in self.logs:
            print(str(log.level) + "     " + str(log.notes) + "       " + str(log.func) + "       " + str(log.time) + "       " + str(log.date))




    def dict(self, filter: typing.Union[None, list] = None):
        _dict = []
        for log in self.logs:
            x = {"Level":log.level,
                 "Notes":log.notes,
                 "Function":log.func,
                 "Datetime":{
                     "Time": log.time,
                     "Date": log.date
                    }
                 }
            _dict.append(x)
        return _dict
    
    def info(self, notes):
        log = Event_Log(1, notes)
        self.logs.append(log)
    
    def debug(self, notes):
        if self._debug == True:
            log = Event_Log("Debug", notes)
            self.logs.append(log)

    def critical(self, notes):
        log = Event_Log(4, notes)
        self.logs.append(log)

    def warning(self, notes):
        log = Event_Log(2, notes)
        self.logs.append(log)

    def error(self, notes):
        log = Event_Log(3, notes)
        self.logs.append(log)
    
    def custom(self, level, notes):
        log = Event_Log(level, notes)
        self.logs.append(log)



class master:
    @classmethod
    def new(cls, logger, default_level:int, verbosity:bool = False, debug:bool = False) -> Log:
        log=Log(default_level=default_level, verbosity=verbosity, debug=debug, name=logger)
        loggers[logger]=log
        return log
    



new = master.new

logger=new("ABC", 3)

@logger.log(3,"ABS",)
def function(number):
    return number


function(3)

x=Event_Log(2, "ABC")

logger.add_log(x)

print(logger.dict())