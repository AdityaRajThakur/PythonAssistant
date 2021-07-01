import ntpath
import sys
import requests
import socket
import pyttsx3
import speech_recognition as sr
import wikipedia as wiki
import time
import datetime
import webbrowser
import os
import subprocess
import random
from plyer import notification
from PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from GUI.MainGUI import Ui_MainWindow
import threading
from UTILITY.main import Coronameter
from twilio.rest import Client
r = sr.Recognizer() 
# r.adjust_for_ambient_noise()
# r.energy_threshold
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 130)

micname = "Microphone (WO Mic Device)"
device_id = 0;
sample_rate = 48000
chunk_size = 2048*2


master = 'Aditya'
SID = os.environ['TWILIO_SID']
TOKEN = os.environ['TWILIO_TOKEN']
# mic_list = sr.Microphone.list_microphone_names()




def info():
    module_name = 'Jarvis'
    version = 2.0
    speak(f'Sir My name is {module_name} , version {version} and created by {master}')



def greet_to():
    hour = int(datetime.datetime.now().strftime('%I'))
    # minute = int(datetime.datetime.now().strftime('%M'))
    meridian = str(datetime.datetime.now().strftime('%p'))
    if hour>=5 and hour<=12 and meridian=='AM':
        speak(f'Good Morning {master}')
    elif hour>=1 and hour<=6 and meridian=='PM':
        speak(f'Good Afternoon {master}')
    elif hour>=6 and hour<=7 and meridian=='PM':
        speak(f'Good Evening {master}')
    else:
        speak(f'Good Night {master}')

def ntfc(title,m):
    notification.notify(title = title , app_name = 'Jarvis',
                                        message = m,
                                        timeout = 6,
                                        app_icon ='E:\\PyAssistant\\brain.ico',
                                        toast = True)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    # engine.save_to_file(text,'speech.mp3')    

def open(path):
    os.startfile(path)

def search():
    # write the search code in here
    pass
def sendmsg(msg):
    try:
        clinet = Client(SID,TOKEN)
        msg = clinet.messages.create(body=msg , to ='+916266641612',from_= "+16129792966")
        print("message sent successfully ")
        speak('message sent successfully ')
    except:
        print("message not sent ")
        speak('message not sent')
def push():
    # writer the push to git hub code here 
    pass 
def report():
    pass
def whatismyip():
    hostcomputer = socket.gethostname()
    ipv4 = socket.gethostbyname(hostcomputer)
    speak(f'Your ip address is {ipv4}')
    ntfc("Your ip address is " , ipv4)
    
def Execution():
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
    time.sleep(.5)
    greet_to()
    down = True
    speak('Wait a few moment intializing the system')
    time.sleep(1)
    speak('System is ready to use')
    
    while(down):
        
        query = Command()
        
        if 'who are you' in query:
            info()  
        elif 'wikipedia' in query:
                print('wikipedia')
                search()
        elif 'shutdown' in query:
                speak('Shuting down the System')
                subprocess.call('shutdown -s -t 5')
        elif 'sleep' in query:
                speak("Sir , let me know when you need me")
                while True:
                    wake = Command()
                    if 'jarvis' in wake:
                        break;
        elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                ntfc('Time',strTime)
                speak(f"Sir, the time is {strTime}")
        elif 'open youtube' in query:
                speak('opening youtube')
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'))
                webbrowser.get('chrome').open('youtube.com')
        elif 'open google' in query:
                speak('opening google')
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'))
                webbrowser.get('chrome').open('Google.com')
        elif 'stackoverflow' in query:
                speak('opening stackoverflow')
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'))
                webbrowser.get('chrome').open('stackoverflow.com')
                #https://www.google.com/search?q=
        elif 'github' in query:
                speak('opening github')
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'))
                webbrowser.get('chrome').open('github.com')
                #https://www.google.com/search?q=
        elif 'open code' in query:
                speak('Openining Code ')
                open('C:\\Users\\Administrator\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')
        elif 'open cmd' in query:
                speak('Opening Command Prompt')
                open('C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk')
        elif 'open chrome' in query:
                speak('Opening Google Chrome')
                open('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
        elif 'take input' in query:
                pass
        elif 'push to github' in query:
                speak('Pushing to Github')
                push()
        elif 'wheather' in query:
                report()
        elif 'covid' in query:
                speak("Wait, a moment sir fetching data")
                covid = Coronameter()
                total_cases = covid.total_case()
                total_death = covid.total_death()
                speak("sir the , report is ")
                ntfc('Total Cases : ',total_cases)
                speak(f'Total Cases around the world are {total_cases}')
                ntfc('Total Death : ',total_death)
                speak(f'and , Total Death around the world are {total_death}')
        elif 'send' in query:
                speak('what do you want to say sir ')
                msg = Command()
                sendmsg(msg)
        elif 'ip address'
        
                
def fun():
    thread.start()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    thread.join()
if __name__ == '__main__':
    thread = threading.Thread(target=Execution)
    fun()
    