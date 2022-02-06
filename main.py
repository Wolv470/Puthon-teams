
import datetime
import json
from hours import Monday_even
from timer import time

json_file=open('ore.json', "r")
load_file=json.load(json_file)
json_file.close()

week=datetime.datetime.now().strftime("%V")
print(week)
date_today = datetime.datetime.today().strftime('%A')
print(date_today)
def time_schedule():
    if (int(week) % 2) == 0:
        while True:
            time()
            stop_hours_list = []
            for materii in load_file[f"{date_today}" + "_even"]:
                print(materii["StartHour"])
                Monday_even(time(), materii, stop_hours_list)
            if time() == ''.join(stop_hours_list[-1:]):
                break


    else:
        while True:
            time()
            stop_hours_list = []
            for materii in load_file[f"{date_today}" + "_odd"]:
                print(materii["StartHour"])
                Monday_even(time(), materii, stop_hours_list)
            if time()  == ''.join(stop_hours_list[-1:]):
                break


if date_today == "Monday":
    time_schedule()
elif date_today == "Tuesday":
    time_schedule()
elif date_today == "Wednesday":
    time_schedule()
elif date_today == "Thursday":
    time_schedule()
elif date_today == "Friday":
    time_schedule()
