import pandas as pd
import pyttsx3 as p
engine = p.init("sapi5")
voice = engine.getProperty("voices")
engine.setProperty('voice',voice[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish_me():
    time= int(datetime.now().hour)
    if 0 <= time >12:
        speak("good morning sir ")
    elif time >=12 and time<18:
        speak("good afternoon sir")
    else:
        speak("good evning sir")
    speak("i am your assistance sir , how can i help you")
    menu = pd.read_csv("C:\\Users\\welcome\\IdeaProjects\\game1\\menu_hostel.csv")
#print(menu)
day = ['Monday','tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
time1 = ['8:30','12:30','5:30','17:02']
import time
from datetime import datetime , date
#Current_day = day[date.today().weekday()]
#Current_time =datetime.now().strftime("%H:%M")
#print(Current_time)


while True:
    c = -1
    c1 = -1
    Current_day = day[date.today().weekday()]
    Current_time =datetime.now().strftime("%H:%M")
    for i in menu['day']:
        c1+=1
        if i == Current_day:
            for j in time1:
                c+=1
                if j ==Current_time:
                    now_time= datetime.now().strftime("%H:%M")
                    print(now_time)
                    wish_me()
                    t1 = time1[c]
                    s = menu[t1]
                    speak("wake up sir It's your time")
                    speak(s[c1])
                    #speak(menu['i'].values[c1])
                    #print(menu['i'].values[c1])
                    break
    break
