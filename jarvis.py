import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os 
import smtplib


engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning,Natali!")

    elif hour>=12 and hour<18:
        speak("Good afternoon,Natali!")
    
    else:
        speak("Good evening,Natali!")

    speak("I am Jarvis,mem. Please tell me how may I help you?")


def takeCommand():
    r = sr.Recognizer()

    while True:

        try:
            with sr.Microphone() as mic:
                r.adjust_for_ambient_noise(mic, duration=0.2)
                audio = r.list(mic)
                text = r.recognize_google(audio)
                text = text.lower()
                print(f"You said...{text}")

        except sr.UnknownValueError():
            print(e)
            r = sr.Recognizer()
            continue

def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail.gmail.com', 'your-password-here')
    server.sendmail('youremail.gmail.com', to, content)
    server.close()
        
if __name__ == "__main__":
    wishMe()
    query = takeCommand()
    
    if 'wikipedia' in query:
        print("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        speak(results)
        speak(results)

    elif 'open you tube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    
    elif 'play music' in query:
        music_dir = "/Users/nataliiagricisin/Documents/music"
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Natali, the time is {strTime}")
    
    elif 'email to send' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "sendEmail@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry, my friend.I am not able to send this email.")