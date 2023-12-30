from log import *

new = master.new

logger = new("ABC", 3)


@logger.error(
    3,
    "ABS",
)
def function(number):
    return number


function(3)

x = Event_Log(2, "ABC")

logger.add_log(x)

print(logger.dict())

print("\n\n")
print(master.get_logggers())
print("\n\n")
logger.print()