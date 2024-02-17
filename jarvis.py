# this is on type of a jarvsi it you start then first set a password

import pyttsx3
import speech_recognition as sr 
import requests
import os
import datetime
import pyautogui
import webbrowser
import random
from pygame import mixer
from plyer import notification
from bs4 import BeautifulSoup
from SearchNow import searchGoogle
from SearchNow import searchYoutube
from SearchNow import searchWikipedia
from GreetMe import greetMe as greetMe
# engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# taccommand
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,10)

    try:
        print("Understanding...")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

# password
for i in range(3):
    a = input("Enter the password to open jarvis [password is jarvis]: - ")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("Welcom sir ! plz speak [jarvis] to load me up")
        break
    elif (i == 2) and (a != pw):
        exit()
    elif (a!=pw):
        print("Try again")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        query = query.replace("service", "jarvis")
        query = query.replace("4:20", "jarvis")
        if "jarvis" in query:
            greetMe()
            while True:
                query = takeCommand().lower()
                # simple a jarvis comand
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break
                elif "open" in query:
                    speak("open, sir...")
                    pyautogui.hotkey('win', 's')
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(1)
                    pyautogui.press('enter')
                # change password
                elif "change password" in query:
                    speak("What's new password")
                    new_pass = input("Enter the new password\n")
                    new_password = open("password.txt", "w")
                    new_password.write(new_pass)
                    new_password.close
                    speak("Done sir")
                    speak(f"Your new password is {new_pass}")
                # schedule your day
                elif "task" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notifi.mp3")
                    mixer.music.play()
                    notification.notify(
                    title = "My schedule :-",
                    message = content,
                    timeout = 15
                    )
                # genrall
                elif "screenshot" in query:
                    pyautogui.hotkey('win', 'alt', 'prtsc')
                elif "screen recording" in query:
                    pyautogui.hotkey('win', 'alt', 'r')
                elif "file" in query:
                    pyautogui.hotkey('win', 'e')
                elif "copy" in query:
                    pyautogui.hotkey('ctrl','c')
                    speak("i am coping")
                elif "paste" in query:
                    pyautogui.hotkey('ctrl','v')
                elif "cut" in query:
                    pyautogui.hotkey('cut', 'x')
                # hello 
                elif "hello"in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                # open dictapp
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                # searchnow
                elif "google" in query:
                    searchGoogle(query)
                elif "youtube" in query:
                    searchYoutube(query)
                elif "wikipedia" in query:
                    searchWikipedia(query)
                # youtube contarol
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Pausing video")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("Playing video")
                elif "mute" in query:
                    pyautogui.press('m')
                    speak("Mute the video")
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("Unmute the video")
                elif "full screen" in query:
                    pyautogui.press("f")
                    speak("The video is now fullscreen")
                elif "exit full screen" in query:
                    pyautogui.press("f")
                    speak("The video is now exit fullscreen")
                elif "moov up" in query:
                    pyautogui.press("l")
                    speak("mooving up")
                elif "moov down" in query:
                    pyautogui.press("j")
                    speak("mooving down")
                # temperature
                elif "temperature" in query:
                    search = "temperature in surat"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current {search} is {temp}")
                # time
                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H,%M")
                    speak(f"sir, the time is {strTime}")
                # remember 
                elif "remember" in query:
                    rememberMsg = query.replace("remeber", "")
                    rememberMsg = query.replace("jarvis", "")
                    speak("you told me" + rememberMsg)
                    remember = open("Remember.txt", "w")
                    remember.write(rememberMsg)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt", "r")
                    speak("you told me " + remember.read())
                
                # song
                elif "song" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1, 2, 3)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open("https://open.spotify.com/playlist/6kKQpgsuE1YxtDa8Sja5Gn?si=84b0d98e2998401b")
                    elif b == 2:
                        webbrowser.open("https://open.spotify.com/playlist/5sdPy37HWnJpM7Pwi6CNBJ?si=a09ef68222894b19")
                    elif b == 3:
                        webbrowser.open("spotify:playlist:33nlpsUyYGA31pwf9Y12du")
                # shutdown
                elif "shutdown" in query:
                    speak("Are you sure you whant to shutdown")
                    shutdown = input("Do you wish to shutdown your computer ? (YES or NO) ")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break 
                elif "sleep" in query:
                    speak ("Are you sure you whant to sleep")
                    sleep = input("Do you wish to sleep your computer ? (YES or NO) ")
                    if sleep == "yes":
                        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                    elif sleep == "no":
                        break

                # match score
                elif "ipl score" in query:
                    from plyer import notification  # pip install plyer
                    import requests  # pip install requests
                    from bs4 import BeautifulSoup  # pip install bs4

                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text, "html.parser")

                    team_elements = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")
                    score_elements = soup.find_all(class_="cb-ovr-flo")
 
                    if team_elements and score_elements:
                        team1 = team_elements[0].get_text() if len(team_elements) > 0 else "Team 1"
                        team2 = team_elements[1].get_text() if len(team_elements) > 1 else "Team 2"
                        team1_score = score_elements[8].get_text() if len(score_elements) > 8 else "N/A"
                        team2_score = score_elements[10].get_text() if len(score_elements) > 10 else "N/A"

                    # Notify or print the scores
                        print(f"{team1}: {team1_score}")
                        print(f"{team2}: {team2_score}")
                    else:
                        print("Couldn't find the required elements on the webpage.")
                # exit
                elif "exit" in query:
                    speak("Thak's sir")
                    exit()