import colours
import typing

class Settings:
    def __init__(self, full:typing.Union[dict, None]=None, colour:typing.Union[None, dict]=None, rest:typing.Union[None, dict]=None, **kwargs) -> None:
        self.colours = colour
        self.settings = {}
        y = full
        z = rest
        x:dict={}
        x["colours"] = self.colours
        self.settings["colours"]=x
        self.settings:dict
        





class Load:
    @classmethod
    def json(cls, file, section:str = "All"):
        import json
        with open(file) as f:
            json_settings=json.loads(f.read())
            json_colours = json_settings["colours"]
            ansi_colors = {}
            i = ["Fore", "Back", "Style"]
            b = ["Date", "Time", "Level", "Func", "Notes"]
            c = 1
            for group in json_colours:
                group = json_colours[group]
                z = {}
                f = "Date"
                for setting in group:
                    setting = group[setting]
                    y = "Fore"
                    x = {}
                    for colour in setting:
                        colour = setting[colour]
                        print(colour)
                        resp = colours.ansi.fore(colour)
                        x[y] = resp
                        try:
                            y=i[i.index(y)+1]
                        except:
                            pass
                    z[f] = x
                    try:
                        f=b[b.index(f)+1]
                    except:
                        pass
                ansi_colors[c] = z
                c+=1
        return Settings(colours=ansi_colors)


class Export:
    @classmethod
    def json(cls):
        pass


Standard:Settings = Load.json("src\\Logging\\standard_settings.json")