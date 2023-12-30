from datetime import time, date, datetime as dt
import typing



class Event_Log:
    Debug = "Debug"

    def __init__(
        self,
        level: int,
        notes: str,
        func=None,
        time: list[int] = [],
        date: list[int] = []
    ):
        self.level_num = level
        self.notes = notes
        self.func = func
        DtTime = [dt.now().hour, dt.now().minute, dt.now().second, dt.now().microsecond]
        self.time = time or DtTime
        DtDate = [dt.now().day, dt.now().month, dt.now().year]
        self.date = date or DtDate
        self.NCDate = ""
        for i in self.date:
            self.NCDate=str(self.NCDate) + str(i) + "/"

        
        self.NCTime = ""
        for i in self.time:
            if not(i > 60):
                self.NCTime=str(self.NCTime) + str(i) + ":"
            else:
                self.NCTime=str(self.NCTime) +str(i)

        self.list = [self.date, self.time, self.level_num, self.notes, self.func]
        self.NCList = [self.NCDate, self.NCTime, self.level_num, self.notes, self.func]


class Atribute_Log:
    def __init__(self, atributes: typing.Union[dict, object]) -> None:
        self.dict = atributes.__dict__
