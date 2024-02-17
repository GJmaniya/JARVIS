import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {
    "paint": "mspaint",
    "word": "winword",
    "excl": "excel",
    "chrome": "chrome",
    "vscod": "code",
    "powerpoint": "powerpnt",
    "spotify": "Spotify",
    "telegram": "Telegram",
}

def openappweb(query):
    speak("opening, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("oen","")
        query = query.replace("jarvis","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")
            
def closeappweb(query):
    speak("closing, sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey('ctrl', 'w')

    elif "2 tab" in query:
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        speak("two tabe is closed")

    elif "3 tab" in query:
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        speak("three tabe is closed")

    elif "4 tab" in query:
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        speak("four tabe is closed")

    elif "5 tab" in query:
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        speak("five tabe is closed")

    elif "close" in query:
        pyautogui.hotkey('alt', 'f4') 
        speak("all tab is closed")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f  /im {dictapp[app]}.exe")

