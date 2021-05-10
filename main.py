import requests
import pyttsx3
import speech_recognition as sr
import wikipedia as wiki  
import time

r = sr.Recognizer()
engine = pyttsx3.init('sapi5')
engine.setProperty('rate',150)

micname = "Microphone (WO Mic Device)"
device_id = 0;
sample_rate = 48000
chunk_size = 2048*2
down = True
mic_list = sr.Microphone.list_microphone_names()

def get_device_id():
    for i,mic in enumerate(mic_list):
        if micname == mic:
            device_id = i ;
            break


def speak(text):
    engine.say(text)
    engine.runAndWait()
    # engine.save_to_file(text,'speech.mp3')    

def search(text):
                speak('searching...')
            print('searching...')
            text = wiki.summary(query , sentences=2)
            print(text)
            time.sleep(0.5)
            speak(text)

def command

while(down):
    
    list = ['what', 'who', 'about']
    with sr.Microphone(device_index=device_id,sample_rate=sample_rate,chunk_size=chunk_size) as source:
        r.adjust_for_ambient_noise(source,duration=1.5)
        print('listening...')
        audio = r.listen(source)
        try:
            print('recognizing..')
            query = r.recognize_google(audio)

        except sr.UnknownValueError:
            print('say again')
            speak('say again')
        except sr.RequestError as e:
            print("cannot request from google wait")
            speak("cannot request form goolge wait")
            
            
    for _ in list:
        if _ in query:

            
            
     
    if 'shutdown' in query:
        print(query)
        down = False
        speak('shutting down the system ')
        break;

    # speak(query)
    print(query)
    
    
