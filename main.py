from tabnanny import check
import requests
from functions.online_ops import *
import pyttsx3
import speech_recognition as sr
#from decouple import config
from datetime import datetime
from functions.os_ops import *
from random import choice
from utils import opening_text,verify_text
from pprint import pprint
import time
import socket

from Offlinecmd import *

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



USERNAME ="Noobtech" #config('USER')
BOTNAME = "zia"#config('BOTNAME')



engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 150)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""
    engine.say(text)
    print(f">>>>>>  {text}")
    engine.runAndWait()
    time.sleep(1)


# Greet the user
def greet_user():
    """Greets the user according to the time"""
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")


# Takes Input from User
def take_user_input():
    #Takes user input, recognizes it using Speech Recognition module and converts it into text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        global query
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if query in verify_text:
            speak(choice(opening_text))
        elif 'exit' in query or 'stop' in query:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query

def exit_stop():
    hour = datetime.now().hour
    if hour >= 21 and hour < 6:
        speak("terminating, Good night buddy, take care!")
    else:
        speak('Have a good day buddy!')
    exit()

    #REACTIVATE
def reactivate():
    b = sr.Recognizer()
    with sr.Microphone() as source:
        print('waiting....')
        b.pause_threshold = 1
        audio = b.listen(source)        

    try:
        print('Recognizing...')
        global react
        react = b.recognize_google(audio, language='en-in')
        #print(react)
        if 'exit' in react or 'stop' in react:
            exit_stop()
        
    except Exception:
        #speak('Sorry, I could not understand. Could you please say that again?')
        reactivate().lower()
    return react

def append_dataonlogfile(logfiledata):
    global logdata
    hr = datetime.now()
    logdata = open("logfile.txt", "a")
    logdata.write(hr.strftime("%c"))
    logdata.write(" >>>>> ")
    logdata.write(logfiledata)
    logdata.write("\n")
    logdata.close()

def append_dataonwordfile(wordfiledata):
    global worddata
    hr = datetime.now()
    worddata = open("wordfile.txt", "a")
    worddata.write(hr.strftime("%c"))
    worddata.write(" ########### ")
    worddata.write(wordfiledata)
    worddata.write("\n")
    worddata.close()

def wakeup():
    react = reactivate().lower()
    
    wakeme = "hello"
    wake = list(wakeme.split())
    #print(wakeme)
    r = list(react.split())
    #print(r)
    while wake[0] == r[0] :
        if len(r) > len(wake):
            query = react
            speak("working out")
            print(query)
            append_dataonlogfile(query)
            listen(query)
            
        elif len(r) == len(wake):
            speak("yes i am here")
            query = take_user_input().lower()
            if 'none' in query:
                pass
            else:
                print(query)
                append_dataonlogfile(query)
                listen(query)
        r =["",""]
    if "none" in react:
        pass        
    elif not wakeme in react:
        append_dataonwordfile(react)

        
def listen(query):
    try:
        print(f'{query}')
        if 'open notepad' in query:
            open_notepad()

        if 'open discord' in query:
            open_discord()

        if 'open command prompt' in query or 'open cmd' in query:
            open_cmd()
                    
        if 'open camera' in query:
            open_camera()
            
        if 'open calculator' in query:
            open_calculator()

        if 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}') 

        if 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)
                
        if 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)
            
        if 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)

        if "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")    

        if "send an email" in query:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")    

        if 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)    

        if "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)    

        if "trending movies" in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies(), sep='\n')    

        if 'news' in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_latest_news(), sep='\n')   

        if 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
        
        if 'search' in query:
            statement = query.replace("search","")
            search(statement)

        if 'open task manager' in query:
            open_taskmanager()
        
        if 'open chrome' in query:
            open_chrome()
        
        if 'open settings' in query:
            open_settings()
        
        if 'open edge' in query:
            open_msedge()
        
        if 'open browser' in query:
            open_browser()
        """            
        if 'close notepad' in query:
            close_notepad()
        
        if 'close camera ' in query:
            close_camera()
        
        if 'close cmd' or 'close command prompt' in query:
            close_cmd()
        
        if 'close task manager' in query:
            close_taskmanager()
        
        if 'close chrome' in query:
            close_chrome()
        
        if 'close settings' in query:
            close_settings()
        
        if 'close edge' in query:
            close_msedge()
        
        if 'close calculator' in query:
            close_calculator()"""

        if 'trash data' in query:
            try:
                trash_logfile()
            except:
                print("NO DATABASE FOUND")     

        else:
            #speak("Something i couldn't fetch now, try again later now now")
            pass    
    
    except:
        speak("Something i couldn't fetch now, try again later")                       


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
    
    def run(self):
        self.mainfunc()

    def mainfunc(self):
            
        #check connection
        
        

        if(check_int() == True):
            #append_dataonlogfile("-----------------Voice Assistant Initiated--------------------")
            #print("Loading AI personal assistant jarvis")
            #speak(f"Loading AI personal assistant {BOTNAME}")
            #greet_user()
            print("online part")
            while True:
                wakeup()
        else:
            print("offline part")
            #append_dataonlogfile("-----------------Voice Assistant Initiated--------------------")
            #speak(f"Loading personal assistant {BOTNAME}")
            #greet_user()
            #speak("you're offline, to get more feature turn to online.")
            #speak("but still you can workout with limited features.")
            #speak("like speak, open command prompt")
            while True:
                Offlinecmd()

#MainThread()
##############################################
def check_int():
    
    try:
        request = requests.get('https://www.google.com/', timeout = 10)
        return True
    except(requests.ConnectionError, requests.Timeout) as Exception:
        return False
        #print("offline")



    
        
    
##############################################




"""class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        #self.ui.setWindowTitle(Qt.FramelessWindowHint)
        #self.ui.start_push.clicked.connect(self.startTask)
        
        

    def startTask(self):
        self.ui.movie=QtGui.QMovie('UIassets\\bg3.jpg')
        self.ui.bgimg.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie('UIassets\\wave-sound-unscreen.gif')
        self.ui.maingif.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie('UIassets\\mic1-unscreen.gif')
        self.ui.micgif.setMovie(self.ui.movie)
        self.ui.movie.start()"""
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainThread()
    sys.exit(app.exec_())