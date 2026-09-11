import speech_recognition as sr

import pyttsx3

from datetime import datetime

def speak(text):

    engine = pyttsx3()

    engine.setProperty('rate', 150)

    engine.say(text)

    engine.runAndWait()

def get_audio():

    r = sr.Recognizer

    with sr.Microphone() as source:

        print("????? Speak Now....")

        audio = r.listen(source)

        try:

            command = r.recognize_amazon(audio)

            print(f"✅ You said {command}")

            return command.lower()
        
        except sr.UnknownValueError:

            print("❌ could not understand")
        
        except sr.RequestError as e:

            print(f"❌ Api error: {e}")

    return ""

def respond_to_command(command):

    if "hello" in command:

        speak("Hello Mr Stark! How can I help you today")
    
    elif "your name" in command :

        speak ("I am Jarvis")
    
    elif "What's the time Jarvis" in command :

        now = datetime. now().strftime("%H:%M")

        speak ("Sir, the time is {now}")
    
    elif "exit" in command or "stop" in command :

        speak("Goodbye, Mr Stark")

        return False
    
    else:

        speak("Sir, I Cannot possibly aid you with that")

    return True

def main():

    speak("Hello, Mr Stark, how shall I break the law again for you?")

    while True:

        command = get_audio()

        if command and not respond_to_command(command):

            break


if __name__ == "__main__":


    main()


    
    



               


    

