from datetime import time, date, datetime as dt
import typing


class Event_Log():

    Debug = "Debug"

    def __init__(self, level:int, notes:str, func=None, time:list[int]=[], date:list[int]=[]):
        self.level = level
        self.notes = notes
        self.func = func
        DtTime = [dt.now().hour, dt.now().minute, dt.now().second, dt.now().microsecond]
        self.time = time or DtTime
        DtDate=[dt.now().day, dt.now().month, dt.now().year]
        self.date = date or DtDate


class Atribute_Log:

    def __init__(self, atributes:typing.Union[dict, object]) -> None:
        self.dict = atributes.__dict__
