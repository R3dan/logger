from colorama import Fore, Back, Style, Cursor
from errors import *


colours_fore = {
    "BLACK":Fore.BLACK,
    "BLUE":Fore.BLUE,
    "CYAN":Fore.CYAN,
    "GREEN":Fore.GREEN,
    "LIGHT BLACK":Fore.LIGHTBLACK_EX,
    "LIGHT BLUE": Fore.LIGHTBLUE_EX,
    "LIGHT CYAN": Fore.LIGHTCYAN_EX,
    "LIGHT GREEN":Fore.LIGHTGREEN_EX,
    "LIGHT MAGENTA":Fore.LIGHTMAGENTA_EX,
    "LIGHT RED":Fore.LIGHTRED_EX,
    "LIGHT WHITE":Fore.LIGHTWHITE_EX,
    "LIGHT YELLOW":Fore.LIGHTYELLOW_EX,
    "MAGENTA":Fore.MAGENTA,
    "RED":Fore.RED,
    "DEFAULT":Fore.RESET,
    "WHITE":Fore.WHITE,
    "YELLOW":Fore.YELLOW,
}

colours_back = {
    "BLACK":Back.BLACK,
    "BLUE":Back.BLUE,
    "CYAN":Back.CYAN,
    "GREEN":Back.GREEN,
    "LIGHT BLACK":Back.LIGHTBLACK_EX,
    "LIGHT BLUE": Back.LIGHTBLUE_EX,
    "LIGHT CYAN": Back.LIGHTCYAN_EX,
    "LIGHT GREEN":Back.LIGHTGREEN_EX,
    "LIGHT MAGENTA":Back.LIGHTMAGENTA_EX,
    "LIGHT RED":Back.LIGHTRED_EX,
    "LIGHT WHITE":Back.LIGHTWHITE_EX,
    "LIGHT YELLOW":Back.LIGHTYELLOW_EX,
    "MAGENTA":Back.MAGENTA,
    "RED":Back.RED,
    "DEFAULT":Back.RESET,
    "WHITE":Back.WHITE,
    "YELLOW":Back.YELLOW,
}


style_fore = {
    "BRIGHT": Style.BRIGHT, 
    "DIM": Style.DIM,
    "DEFAULT": Style.NORMAL
}


class ansi:
    @classmethod
    def __init__(cls):
        pass


    @classmethod
    def fore(cls, colour:str):
        try:
            return colours_fore[colour.upper()]
        except:
            raise InvalidForeColour
        
    @classmethod
    def back(cls, colour:str):
        try:
            return colours_back[colour.upper()]
        except:
            raise InvalidBackColour
        
    @classmethod
    def style(cls, style:str):
        try:
            return style_fore[style]
        except:
            raise InvalidStyle
        
    @classmethod
    def reset_all(cls):
        return Style.RESET_ALL