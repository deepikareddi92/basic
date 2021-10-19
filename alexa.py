import pyttsx3
from selenium_web import infow
from youtube import music
from weather import *
import datetime
import randfacts

engine = pyttsx3.init()

rate=engine.getProperty("rate")
engine.setProperty("rate",130)

voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello Madam,  I am your voice assistant, how are you?")
text=input("Hello Madam,  I am your voice assistant, how are you?: ")
if "what" and "about" and "you" in text:
    speak("I am having a good day madam")
speak("what can i do for you?")
text1=input("what can i do for you?")

if "information" in text1:
    speak("You need information related to which topic?")
    info=input("You need information related to which topic?")
    speak("searching {} in wikipedia".format(info))
    print("searching {} in wikipedia".format(info))
    assist = infow()
    assist.get_info(info)

elif "play" and "video" in text1:
    speak("You want me to play which video?")
    vid=input("You want me to play which video?")
    speak("playing {} on youtube".format(vid))
    print("playing {} on youtube".format(vid))
    assist1 = music()
    assist1.get_info(vid)

elif "temperature" in text1:
    speak("Please mention the city name")
    text2=input("Please mention the city name")
    temp1 = temp(text2)
    speak("Temperature in {} is {}".format(text2, temp1))
    print("Temperature in {} is {}".format(text2, temp1))

elif "date" in text1:
    today=str(datetime.date.today())
    speak("Today's date is "+today)
    print("Today's date is " + today)

elif "time" in text1:
    hour=str(datetime.datetime.now().hour)
    minute=str(datetime.datetime.now().minute)
    speak("Time is "+hour+"  hour and  "+minute+" minutes")
    print("Time is " +hour+" hour and "+minute+" minutes")

elif "fact"  in text1:
    speak("sure madam, ")
    x=randfacts.getFact()
    print(x)
    speak("Did you know that, "+x)



