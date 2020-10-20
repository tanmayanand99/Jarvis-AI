import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import imaplib,email
import pandas as pd
import subprocess
import subprocess
import sys
import subprocess

GMAIL_ID=""                                             #ENTER YOUR GMAIL ID
GMAIL_PSWD=""                                           #ENTER YOUR GMAIL PASSWORD

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("Hello, I am Jarvis How may i help you")

def takeCommand():
    #microphone input
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, subject, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(GMAIL_ID,GMAIL_PSWD)
    server.sendmail(GMAIL_ID, to , f"Subject:{subject}\n\n{content}")
    server.close()

if __name__=='__main__':
    while True:
        query=takeCommand().lower()
        if 'hi jarvis' in query:
            wishMe()
            while True:
                query=takeCommand().lower()
                
                if 'wikipedia' in query:
                    speak('searching wikipedia...')
                    query=query.replace("wikipedia","")
                    results=wikipedia.summary(query, sentences=2)
                    print(results)
                    speak(f"According to Wikipedia {results}")

                elif 'hey jarvis' in query:
                    wishMe()
                elif 'open youtube' in query:
                    speak('opening youtube')
                    webbrowser.open("https://www.youtube.com/")

                elif 'open google' in query:
                    speak('opening google')
                    webbrowser.open("https://www.google.com/")
                
                elif 'open stackoverflow' in query:
                    speak('opening stackoverflow')
                    webbrowser.open("https://www.stackoverflow.com/")

                elif 'play music' in query:
                    webbrowser.open("")                                     # LINK OF YOUR YOUTUBE PLAYLIST

                elif 'the time' in query:
                    strtime=datetime.datetime.now().strftime("%I:%M:%p")
                    speak(f"the time is {strtime}")
                
                elif 'open code' in query:
                    path=""                                                 # PATH OF YOUR VS CODE EDITOR
                    # print(path)
                    try:
                        os.startfile(path)
                    except Exception as e:
                        print(e)
                        speak("sorry cant open")
                    
                    # speak("Opening Visual Studio Code")

                elif 'send email' in query:
                        speak("To whom should i send email")
                        name=takeCommand().lower()
                        df=pd.read_excel("")                                # PATH OF THE DATA.XLSX FILE
                        for index,item in df.iterrows():
                            if item['Name'] in name:
                                to=item['Email']
                                speak("What should I say?")
                                content=takeCommand()
                                speak("What should be the subject")
                                subject=takeCommand()
                                sendEmail(to, subject, content)
                                speak("Email has been sent!")  
                                break
                elif 'the date today' in query:
                    now = datetime.datetime.now()
                    day=now.strftime("%A")
                    speak(f"today is {day}")
                elif 'open my folder' in query:
                    speak('opening your folder')
                    os.subprocess('')                                       # PATH OF YOUR FOLDER
                elif 'quit' in query:
                    exit()
        elif 'quit' in query:
            exit()       