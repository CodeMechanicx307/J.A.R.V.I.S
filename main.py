import pygame
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import google.generativeai as genai
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "YOUR_NEWS_API"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):

    genai.configure(api_key="YOUR_GEMINI_DEVELOPER_API")
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": command},
            {"role": "model", "parts": "You are a virtual Assistant named Jarvis , skilled in general tasks like Alexa and GPT-4 give short responses please"},
        ]
)
    response =  chat.send_message(chat.history[1])
    return response.text

def processcommand(c):
    if 'open google' in c.lower():
        webbrowser.open("https://google.com")
    elif 'open facebook' in c.lower():
        webbrowser.open("https://facebook.com")
    elif 'open youtube' in c.lower():
        webbrowser.open("https://youtube.com")
    elif 'open github' in c.lower():
        webbrowser.open("https://github.com")
    elif 'open eshikhon' in c.lower():
        webbrowser.open("https://eshikhon.com/")
    elif 'open gmail' in c.lower():
        webbrowser.open("https://mail.google.com/")
    elif 'open fast' in c.lower():
        webbrowser.open("https://fast.com/")
    elif 'open wiki' in c.lower():
        webbrowser.open("https://wikipedia.org/")
    elif 'show music' in c.lower():
        print(musicLibrary.music)
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=1b1fcbcbb0f746e784675aa44b3259a8")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles',[])
            for article in articles:
                speak(article['title'])
    else:
        output = aiprocess(c)
        speak(output)
    
    
   

    


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    # obtain audio from the microphone
    while True:
        r = sr.Recognizer()
       
        print("Recognizing...")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word =  r.recognize_google(audio)
            if (word.lower() == 'jarvis'):
                speak('Yeh')
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command =  r.recognize_google(audio)
                    processcommand(command)
        except Exception as e:
            print("Error; {0}".format(e))
