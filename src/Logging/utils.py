import platformdirs
import platform
import typing
import os



try:
    APP_AUTHOR = "R3dans"
    APP_NAME = "Logging"
    USER_CONFIG = platformdirs.user_config_dir(APP_NAME, APP_AUTHOR)
    os.makedirs(USER_CONFIG)
except:
    pass