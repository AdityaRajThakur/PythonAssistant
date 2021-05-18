import requests
import pyttsx3
import speech_recognition as sr
import wikipedia as wiki
import time
import datetime
import webbrowser
import os
from plyer import notification
import random


r = sr.Recognizer() 
# r.adjust_for_ambient_noise()
# r.energy_threshold
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)

micname = "Microphone (WO Mic Device)"
device_id = 0;
sample_rate = 48000
chunk_size = 2048*2
down =  True
greet = True
master = 'Aditya'
mic_list = sr.Microphone.list_microphone_names()
list = ['what', 'who', 'about']


def get_device_id():
    for i, mic in enumerate(mic_list):
        if micname == mic:
            device_id = i;
            break
def info():
    module_name = 'Jarvis'
    version = 2.0
    speak(f'Sir My name is {module_name} , version {version} and created by {master}')

def greet_to():
    hour = int(datetime.datetime.now().strftime('%I'))
   
    minute = int(datetime.datetime.now().strftime('%M'))
    meridian = str(datetime.datetime.now().strftime('%p'))
    
    if hour>=5 and hour<=12 and meridian=='AM':
        speak(f'Good Morning {master}')
    elif hour>=1 and hour<=6 and meridian=='PM':
        speak(f'Good Afternoon {master}')
    elif hour>=6 and hour<=7 and meridian=='PM':
        speak(f'Good Evening {master}')
    else:
        speak(f'Good Night {master}')

def ntfc(title,messag):
    notification.notify(title = title , messag = messag ,timeout = 2);

def speak(text):
    engine.say(text)
    engine.runAndWait()
    # engine.save_to_file(text,'speech.mp3')    

def opencode():
        vscodepath = 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
        os.startfile(vscodepath)


def search():
    speak('What do you want to search from wikipeadia')
    query = Command()
    speak('searching in wikipeadia')
    text = wiki.summary(query , sentences=1)
    speak('Search complete... result may or may not be accurate')
    print(text)
    time.sleep(0.5)
    speak(text)

def Command():
    with sr.Microphone(device_index=device_id,sample_rate=sample_rate,chunk_size=chunk_size) as source:
        r.adjust_for_ambient_noise(source , duration=2);
        print('listening..')
        # r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = (r.recognize_google(audio, language='en-in')).lower()
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak(" I can't hear you...")
        print("I can't hear you... sir")  
        return "None"
    return query   



if __name__ == '__main__':
    greet_to()
    speak('wait a moment intializing the system')
    while(down):
        
        query = Command()
        
        if 'who are you' in query:
            info()  
        
        elif 'wikipedia' in query:
            print('wikipedia')
            search()
        elif 'shutdown' in query:
            print(query)
            down = False
            speak('shutting down the system ')
            break;
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            speak('opening stackoverflow')
            webbrowser.open("stackoverflow.com")   
        elif 'open code' in query:
            speak('Openining Code ')
            opencode();

    

        
    
