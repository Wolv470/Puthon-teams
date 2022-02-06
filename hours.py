
import subprocess
import pyautogui as pg
from timer import sleep
from teams import teams
import datetime
from datetime import timedelta
from teams import hidden
from teams import your_group

def Monday_even(curent_time, materii, stop_hours_list):
    if curent_time >= materii["StartHour"] and curent_time < materii["StopHour"]:
        materia = materii["Materia1"]
        print(materia)
        finish_hour = materii["StopHour"]
        print(materii["StartHour"])
        subprocess.call(r'C:\Users\alinb\AppData\Local\Microsoft\Teams\Update.exe --processStart "Teams.exe"')
        sleep(8)
        teams()
        sleep(2)



        pg.click(pg.locateOnScreen(f"screens_for_hours/{materia}.png"))
        sleep(2)
        pg.click(pg.locateOnScreen("acces_folder/join.png"))
        sleep(2)
        hidden()
        sleep(2)
        your_group()
        sleep(2)
        pg.click(pg.locateOnScreen("acces_folder/join.png"))
        sleep(2)
        try:
            sleep(2)
            pg.click(pg.locateOnScreen("acces_folder/microfon.png"))
        except:
            pass

        pg.click(pg.locateOnScreen("acces_folder/join.now.png"))
        sleep(2)

        date_obs = datetime.datetime.strptime(curent_time.replace(":", ""), "%H%M")
        print(date_obs)
        date_obs2 = datetime.datetime.strptime(finish_hour.replace(":", ""), "%H%M")
        print(date_obs2)

        diff = date_obs2 - date_obs
        total = diff.total_seconds()
        value = timedelta(seconds=total-30)
        print(value)
        sleep(value.total_seconds())


        time_now = datetime.datetime.now().strftime("%H:%M")
        print(time_now)
        if time_now <= finish_hour:
            sleep(2)
            pg.click(pg.locateOnScreen("acces_folder/leave.png"))

        stop_hours_list.append(materii["StopHour"])
    return stop_hours_list
