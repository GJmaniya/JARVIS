from fnmatch import translate
from time import sleep
from googletrans import Translator
import googletrans #pip install googletrans
from gtts import gTTS
import googletrans
import pyttsx3
import speech_recognition 
import os
from playsound import playsound
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def translategl(query):
    speak("SURE SIR")
    print(googletrans.LANGUAGES)
    translator = Translator()
    speak("Choose the language in which you want to translate")
    b = input("To_Lang :- ")   
    text_to_translate = None
    retry_count = 3  # Number of times to retry
    while retry_count > 0:
        try:
            text_to_translate = translator.translate(query, src="auto", dest=b)
            break  # Exit the loop if translation succeeds
        except Exception as e:
            print("Error during translation:", e)
            print("Retrying...")
            retry_count -= 1
            time.sleep(2)  # Wait for 2 seconds before retrying

    if text_to_translate is not None:
        text = text_to_translate.text
        try:
            speakgl = gTTS(text=text, lang=b, slow=False)
            speakgl.save("voice.mp3")
            playsound("voice.mp3")
            
            time.sleep(5)
            os.remove("voice.mp3")
        except Exception as e:
            print("Error during speech synthesis:", e)
            print("Unable to translate")
    else:
        print("Translation failed after multiple attempts.")

