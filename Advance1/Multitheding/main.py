# thread = a flow execution. Like a separate order of instruction.
#           however, each thread take a turn running to achieve concurrency
#           GIL = (global interpreter lock),
#           allows only one thread to hold the control of the python interpreter at any one time
#                   it is used in CPython and other implementations that use the C call stack as the


# cpu bound = program/task spends most of its time waiting for internal events (cpu intensive)
#               use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (users input/web scraping)
#              use multithreading

import threading
import time


def eat():
    time.sleep(3)
    print("i have finished dinner.!")


def gaming():
    time.sleep(5)
    print("I am i played game")


def study():
    time.sleep(4)
    print("I studeid python!")


eat()
gaming()
study()

# print(threading.active_count())
# print(threading.enumerate())
