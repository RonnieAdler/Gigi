import datetime

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import vlc  
import pafy 
  

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say("Hi, My name is Gigi. What is your name")

engine.runAndWait()


def talk(text):
    # engine.say(text)
    print("Gigi:",text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            # print('ki')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command1 = command.lower()
            if 'gigi' in command1:
                command1 = command1.replace('gigi', '')
                talk(command1)
                return command1
            else:
                return 0

    except():
      pass


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'who' or 'what' or 'search' or 'search about' in command:
        person = command.replace('who is' or 'what is' or 'search about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'help' in command:
        url = ""
        video = pafy.new(url) 
        best = video.getbest() 
        media = vlc.MediaPlayer(best.url) 
        media.play() 
        
    elif 'date' or 'love' in command:
        talk('I am in relationship with Jarvis')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
