class Error(Exception):
    """Base class for all logging errors"""


class InvalidForeColour(Error):
    """Raised when an invalid fore colour is given"""

class InvalidBackColour(Error):
    """Raised when an invalid back colour is given"""

class InvalidStyle(Error):
    """Raised when an invalid style is given"""