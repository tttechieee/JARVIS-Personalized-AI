import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good afternoon")
    else:
        speak("Good Evening")
    speak("I'm System sir, Tell me how can I help you?")

def takecommand():
    #This function takes input form microphone and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #seconds of non-speaking audio before a phase is considered complete
        audio = r.listen(source)
    
    try:
        print("Recognizing..")
        query=r.recognize_google(audio, Language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        #print(e)

        print('Say that again please')
        return "none"
    return query

'''def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()'''

if __name__== "__main__":
    wishme()
    while True:
        query = takecommand().lower()

    #Logic for executing tasks based query
    if 'wikipedia' in query:
        speak("Searching wikipedia...")
        query=query.replace("wikipedia", "")
        result= wikipedia.summary(query, sentence=2)
        speak("According to Wikipedia")
        prints(result)
        speak(result)
    elif 'open youtbe' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
            webbrowser.open("google.com")
    elif 'play music' in query:
            music_dir = 'C:\\Users\\Admin\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
    elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
    '''elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")'''



