import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime
import math
import webbrowser
import pyjokes


listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Hey! I am Granzo")
            talk("Hey! I am Granzo")
            print("Ask me a question.....")
            talk("Ask me a question.....")
            print("listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'hey granzo' in command:
                command=command.replace('hey granzo','')
                print(command)
    except:
        pass
    return command

def run_assistant():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('Sure playing'+ song)
        talk('On YouTube')
        pywhatkit.playonyt(song)
    
    elif 'hello' in command:
        talk("Hi.")
    
    elif 'will i get a girlfriend' in command:
        talk("Maybe you should ask this question to yourself.")

    elif 'will i get a boyfriend' in command:
        talk("Maybe you should ask this question to yourself.")

    elif 'how are you' in command:
        talk("I am doing good. Hope you are doing good toooo")

    
    elif 'open youtube' in command:
        talk("Here you go to Youtube\n")
        webbrowser.open("https://www.youtube.com/")

    elif 'alexa' in command:
        talk("Well....she is cute. I really like her voice. She's probably my sister but from Amazon ")
    
    elif 'what do you think about google assistant' in command:
        talk("She's well trained and I really admire her passion to educate people")

    elif 'what do you think about siri' in command:
        talk("She has the sweetest voice...")


    
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I : %M %p')
        print(time)
        talk('Current time is' + time)

    
    elif 'what is the meaning of' in command:
        search=command.replace('what is the meaning of','')
        talk("Sure! Here is what I found through search")
        pywhatkit.search(search)

    elif 'what do you mean by' in command:
        search=command.replace('what do you mean by','')
        talk("Sure! Here is what I found through search")
        pywhatkit.search(search)
    
    elif 'what do you think about' in command:
        search=command.replace('what do you think about','')
        talk("Sure! Here is what I found through search")
        pywhatkit.search(search)
    
    elif 'what is' or 'how to' in command:
        search=command.replace('what is','')
        talk("Sure! Here is what I found through search")
        pywhatkit.search(search)

    

    elif 'who made you' in command:
        talk("I was created by Kunal Shenoy")

    elif 'can you see me' in command:
        talk("Hehehe...that's an intresting question")
        talk("Joke's apart...I can't see you!!")

    elif 'do you know where i stay' in command:
        talk("I am not capable of knowing your location without your permission")

    elif 'joke' in command:
        talk("Here's an interesting joke!")
        talk(pyjokes.get_joke())

    elif 'are you dumb' in command:
        talk("I maybe dumb but surely less than you")
    
    elif 'will chat gpt replace programmers'or 'can chat gpt replace programmers' in command:
        talk("ChatGPT cannot replace programmers. Although it can facilitate")



while True:
    run_assistant()