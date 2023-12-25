import platformdirs
import platform
import typing
import os

DEBUG=True

try:
    APP_AUTHOR = "R3dans"
    APP_NAME = "Pydir"
    USER_CONFIG=platformdirs.user_config_dir(APP_NAME, APP_AUTHOR)
    os.makedirs(USER_CONFIG)
except:
    pass


def debug(values:object, sep:typing.Union[str, None] = " ", end:typing.Union[str, None] = "\n", file = None,flush=False):
    if DEBUG:

        print(values, sep=sep, end=end, file=file, flush=flush)