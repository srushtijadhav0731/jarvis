import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import instaloader
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import cv2
import wikipedia
import random
import webbrowser
import pywhatkit
import smtplib
import sys
import pyjokes
import pyautogui
import instadownloader

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
# print("voices")

# to speak
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to take command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")

    except Exception as e:
        speak("say that again please...")
        return "None"
    return query

# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour > 12 and hour < 18:
        speak("good afternoon")
    else:
        speak(" good evening")
    speak("I am jarvis sir. please tell me how may i help you....")

# foe news update
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=cc5accdf16894f54a29002f4717c0e2d'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day =["first", "second", "third", "fourth", "fifth", "sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: , {head[i]}")



if __name__ == '__main__':
    wish()

    while True:
    # if 1:
        query = takeCommand().lower()

        if "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "open notepad" in query:
            npath = "C:\\windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")


        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif "play music" in query:
            music_dir = "C:\\Users\\ujjwala\\OneDrive\\Desktop\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open spotify" in query:
            webbrowser.open("www.spotify.com")


        elif "open google" in query:
            speak("sir, what should i search on google")
            cm =takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")




        elif "play song on youtube" in query:\
        pywhatkit.playonyt("Don't fight the feeling")




        elif "send email to me" in query:
            speak("mam, what should i say")
            query= takeCommand().lower()
            if "send a file" in query:
                email = "srushtijadhav0731@gmail.com"
                password = "srushti0731"
                send_to_email = 'srushtijadhav061@gmail.com'
                speak("okay mam, what is the subject for this email")
                query:takeCommand().lower()
                subject = query
                speak("and mam , what is the message for this email")
                query2 = takeCommand().lower()
                message = query2
                speak("mam,please enter the correct path of the file into the shell")
                file_location = input("please enter the path here")

                speak("please wait ,i am sending email now")

                msg =MIMEMultipart()
                msg['From '] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message,'plain'))

                # setup the attachment
                filename = os.path.basename(file_location)
                attachment = open(file_location , "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename = %s" %filename)

                # attach the attachment to the MIMEMultiproject object
                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 535)
                server.starttls()
                server.login(email,password)
                text = msg.as_string()
                server.sendmail(email, send_to_email,text)
                server.quit()
                speak("email has been sent to bunny")
            else:
                email = 'srushtijadhav0731@gmail.com'
                password = 'srushti0731'
                send_to_email = 'srushtijadhav061@gmail.com'
                message= query

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email,password)
                server.sendmail(email,send_to_email,message)
                server.quit()
                speak("email has been sent to your friend")

        elif "tell me news" in query:
            speak("please wait sir , fetching the latest news")
            news()

        elif "where i am now" in query or "where are we now" in query:
            speak("wait mam,let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                state = geo_data['state']
                country = geo_data['country']
                speak(f"sir i am not sure,but i think we are in {city} city of {state} {country}")
            except Exception as e:
                speak("sorry sir ,Due to network issue i am not able to find where we are.")
                pass

        elif "you can sleep now" in query:
            speak("thank you for using me sir,  have a good day.")
            sys.exit()

        elif "instagram profile" in query or "profile on instagram" in query:
            speak("mam please enter the user name correctly")
            name = input("Enter Username Here: ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"mam,here is the profile of the user {name}")
            time.sleep(5)
            speak("mam. would you like to download profile picture of this account.")
            condition = takeCommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name,profile_pic_only = True)
                speak("I am done mam, profile picture is saved in our main folder.now i am ready for next task")
            else:
                pass

        elif "take a screenshot" in query or "take screenshot" in query:
            speak("mam, please tell me name for this screenshot file")
            name = takeCommand().lower()
            speak("mam please hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)

            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done mam, the screenshot is saved in our main folder.now i am ready for next task")
        





















        elif "you can sleep now" in query:
            speak("thank you for using me sir,  have a good day.")
            sys.exit()

        # to close application
        elif "close notepad" in query:
            speak("okay sir,closing notepad")
            os.system("taskkill/f /im notepad.exe")


         # to set an alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
                music_dir = "C:\\Users\\ujjwala\\OneDrive\\Desktop"
                os.startfile(os.path.join(music_dir,songs[0]))


         # to switch window
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")



         # to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shutdown " in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")






    else:
            pass
