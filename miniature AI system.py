import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour <=12 :
        speak("GOOD MORNING!")
    elif hour>12 and hour <=18 :
        speak("GOOD AFTERNOON!")
    else :
        speak("GOOD EVENING!")
    speak("hello!,I am jarvis sir.")
    speak("How may i help you?")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")


        audio = r.listen(source)

    try:
        print("recognizing...")
        query=r.recognize_google(audio,language='en_in')
        print(f"user said:{query}\n")
    except Exception as e:
        #print(e)
        print("say that again please..")
        return "None"
    return query


if __name__ == '__main__':
        wishme()
        while True:
          query=takecommand().lower()


          if 'wikipedia' in query:
              speak("searching wikipedia..")
              query = query.replace("wikipedia","")
              results = wikipedia.summary(query, sentences=2)
              speak("According to wikipedia")
              print(results)
              speak(results)

          elif 'open google' in query:
              speak("opening google")
              webbrowser.open("google.com")
          elif 'open youtube' in query:
              speak("opening  youtube")
              webbrowser.open("youtube.com")
          elif 'i want to code' in query:
              speak("opening hackerearth")
              webbrowser.open("hackerearth.com")
          elif 'shut up' in query:
              speak("maaf kariyega sir")

          elif 'time' in query:
              strtime= datetime.datetime.now().strftime("%H:%M:%S")
              print(strtime)
              speak(strtime)
          
          elif 'open github' in query:
					    speak("opening github")
							webbrowser.open("github.com")
					"""
					elif 'play music' in query:
              (directory_name)= "path of the file containing songs"
              print(songs)
             os.startfile(os.path.join((directory_name),song[0])
					"""
							
