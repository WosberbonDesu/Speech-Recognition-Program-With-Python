import speech_recognition as sr
import time
from datetime import datetime
import webbrowser
from gtts import gTTS
from playsound import playsound
import random
import os

r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ""
        try:
            speak = r.recognize_google(audio, language="en=EN")
        except sr.UnknownValueError:
            speak("Sorry didn't understand")
        except sr.RequestError:
            speak("Sorry program didn't work")
        return voice
def response(voice):
    if "nasılsın" in voice:
        speak("Thank you what about you")
    if "saat kaç?" in voice:
        speak(datetime.now().strftime("%H:%M:%S"))
    if "arama yap" in voice:
        search = record("what do you want")
        url = "https://google.com/search?q="+search
        webbrowser.get().open(url)
        print(search+" i found for")
    if "done" or "see you" in voice:
        speak("See you")
        exit()
def speak(string):
    tts = gTTS(string,lang="en")
    rand = random.randint(1,10000)
    file = "audio-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)
speak("How can i help you")
time.sleep(1)
while 1:
   voice = record()
   print(voice)
   response(voice)
