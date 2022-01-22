import cv2
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import smtplib
from email.message import EmailMessage
import pyautogui
import os
import gtts
import playsound
import googletrans
from pd import password
from pd import talk
from time import sleep

try:
    pas = input('password please:')
    if pas != password:
        a = 'provide the correct password!!!!!!!!!!!!!!!!!!!'
        talk(a)
        print(a)
    else:
        talk('welcome')
        print('welcome')

        listener = sr.Recognizer()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        jokes = pyjokes.get_joke('en', 'neutral')
        translator = googletrans.Translator()
        cap = cv2.VideoCapture(0)


        def talk(text):
            engine.say(text)
            engine.runAndWait()


        def take_command():
            try:
                with sr.Microphone() as source:
                    print('listening...')
                    voice = listener.listen(source)
                    command = listener.recognize_google(voice)
                    command = command.lower()
                    if 'alexa' in command:
                        print(command)
                        command = command.replace('alexa', '')
            except:
                pass
            return command

        def send_email(receiver, subject, message):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('rakibshakib007@gmail.com', "mnpqzrpctgkatdxj")
            email = EmailMessage()
            email['From'] = 'rakibshakib007@gmail.com'
            email['To'] = receiver
            email['Subject'] = subject
            email.set_content(message)
            server.send_message(email)


        email_list = {
            'rakib': 'asibur247@gmail.com'
        }

        def run_alexa():
            try:
                command = take_command()
                print(command)
                if 'play' in command:
                    song = command.replace('play', '')
                    talk('playing ' + song)
                    pywhatkit.playonyt(song)
                elif 'time' in command:
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    talk('Current time is ' + time)
                elif 'tell me about' in command:
                    person = command.replace('according to wikipedia', '')
                    info = wikipedia.summary(person, 1)
                    print(info)
                    talk(info)
                elif 'how are you?' in command:
                    talk('i am fine and you')
                elif 'joke' in command:
                    converted_jokes = translator.translate(jokes, dest='bn')
                    print(converted_jokes.text)
                    print(jokes)
                    converted_audio = gtts.gTTS(converted_jokes)
                    converted_audio.save('funny jokes.mp3')
                    playsound.playsound('funny jokes.mp3')
                    pyautogui.typewrite(jokes)
                elif 'open youtube' in command:
                    talk('opening youtube')
                    webbrowser.open('https://www.youtube.com/')
                elif 'open email' in command:
                    talk('opening email')
                    webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
                elif 'open google' in command:
                    talk('opening google')
                    webbrowser.open('https://www.google.com/')
                elif 'open facebook' in command:
                    talk('opening facebook')
                    webbrowser.open('https://www.facebook.com/')
                elif 'search' in command:
                    talk('search')
                    pywhatkit.search(command)
                elif 'open my course' in command:
                    talk('opening your course')
                    course_Path = 'C:\\Users\\RAKIB\\Downloads\\2021 Complete Python Bootcamp From Zero to Hero in Python'
                    os.startfile(course_Path)
                elif 'screenshot' in command:
                    talk('screenshot')
                    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                    file_name = f'screenshort{time_stamp}.png'
                    pywhatkit.take_screenshot(file_name)

                elif 'what is your name' in command:
                    talk('my name is alexa')
                elif 'photo' and 'pic' in command:
                    while True:
                        _, frame = cap.read()
                        sleep(3)
                        cv2.imshow(frame, 'cam')
                        if cv2.waitKey(10) == ord('q'):
                            break
                elif 'stop' in command:
                    pyautogui.press('q')
                elif 'down' in command:
                    talk('....')
                    pyautogui.keyDown('PgDn')

                elif 'up' in command:
                    talk('....')
                    pyautogui.keyUp()

                elif 'send email' in command:
                    try:
                        talk('To Whom you want to send email')
                        name = take_command()
                        receiver = email_list[name]
                        print(receiver)
                        talk('What is the subject of your email?')
                        subject = take_command()
                        talk('Tell me the text in your email')
                        message = take_command()
                        send_email(receiver, subject, message)
                        talk('Your email is sent')
                    except Exception as e:
                        print(e)
                        talk('i am not able to send email')

                else:
                    talk('Please say the command again.')
            except:
                pass


        def wish_me():
            hour = int(datetime.datetime.now().hour)
            if hour >=0 and hour<12:
                talk('good morning, How can i help you?')
            elif hour>=12 and hour<18:
                talk('good after noon ,  How can i help you?')
            else:
                talk('good evening ,  How can i help you?')
        wish_me()


        while True:
            run_alexa()
except Exception as E:
    print(E)
