import datetime
from time import sleep

def time():
    curent_time = datetime.datetime.now().strftime("%H:%M")
    print(curent_time)
    print("\n")
    sleep(2)
    return curent_time