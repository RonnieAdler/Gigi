import datetime

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyaudio
import websockets
import pyjokes
# import vlc  
# import pafy 

b=True
  

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say("Hi, My name is Kali. Nice to meet you. Give me a command.")


engine.runAndWait()


def talk(text):
    # engine.say(text)
    print("Kali:",text)
    engine.say(text)
    # run_alexa(text)
    engine.runAndWait()




def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            # print('ki')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command1 = command.lower()
            print(command1)
            if "kali" in command1:
                command1 = command1.replace("kali", "")
                # talk(command1)
                run_alexa(command1)
                # return command1
            else:
                return 0

    except():
      pass


def run_alexa(command):
    # command=text
    # command = take_command()
    # print(command)

    if "exit" in command:
        talk("Bye, Take Care")
        b=False
        return 0

    elif "play" in command:
        song = command.replace("play", '')
        talk("playing"+song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk("Current time is" + time)
    elif "who" or "what" or "search" or "search about" or "about" in command:
        person = command.replace("who is" or "what is" or "search about", '')
        info = wikipedia.summary(person, 1)
        # print("Gigi: "+info)
        talk(info)
    # elif "help" in command:
    #     # url = ""
    #     # video = pafy.new(url) 
    #     # best = video.getbest() 
    #     # media = vlc.MediaPlayer(best.url) 
    #     # media.play() 
        
    elif "date" or "love" in command:
        talk('I am in relationship with Jarvis')
    elif "joke" in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')
    


while b==True:
    take_command()
    # engine.say("Give me a command")
