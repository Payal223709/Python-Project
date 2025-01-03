import speech_recognition as sr
import datetime
import os
import random
import webbrowser
import sys
import pyttsx3
import wikipedia
import wolframalpha

# Text To Speechp


engine = pyttsx3.init('sapi5')

#client = wolframalpha.Client('LU8ERW-WXRTV5K7JT')

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)



def speak(audio):  # here audio is var which contain text
    engine.say(audio)

    engine.runAndWait()



def wish():

    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:

        speak("good morning sir i am virtual assistent alais")

        print("good morning sir i am virtual assistent alais")

    elif hour >= 12 and hour < 18:

        speak("good afternoon sir i am virtual assistent alais")

        print("good afternoon sir i am virtual assistent alais")

    else:

        speak("good night sir i am virtual assistent alais")

        print("good night sir i am virtual assistent alais")


# now convert audio to text

#

def takecom():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listning....")

        audio = r.listen(source)

    try:

        print("Recognising.")

        text = r.recognize_google(audio, language='en-in')

        print(text)

    except Exception:  # For Error handling

        speak("error...")

        print("Network connection error")
        return "none"

    return text



# for main funcation

if __name__ == "__main__":

    wish()

    while True:

        query = takecom().lower()


        if "wikipedia" in query:

            speak("searching details....Wait")

            query.replace("wikipedia", "")

            results = wikipedia.summary(query, sentences=2)
            print(results)

            speak(results)

        elif 'open youtube' in query or "open video online" in query:

            webbrowser.open("www.youtube.com")

            speak("opening youtube")

            print("opening youtube")

        elif 'open github' in query:

            webbrowser.open("https://www.github.com")

            speak("opening github")

            print("opening github")

        elif 'open facebook' in query:

            webbrowser.open("https://www.facebook.com")

            speak("opening facebook")

            print("opening facebook")

        elif 'open instagram' in query:

            webbrowser.open("https://www.instagram.com")

            speak("opening instagram")
            print("opening instagram")

        elif 'open google' in query:

            webbrowser.open("https://www.google.com")

            speak("opening google")
            print("opening google")


        elif 'open yahoo' in query:

            webbrowser.open("https://www.yahoo.com")

            speak("opening yahoo")

            print("opening yahoo")


        elif 'open gmail' in query:

            webbrowser.open("https://mail.google.com")

            speak("opening google mail")
            print("opening google mail")


        elif 'open snapdeal' in query:

            webbrowser.open("https://www.snapdeal.com")

            speak("opening snapdeal")
            print("opening snapdeal")



        elif 'open amazon' in query or 'shop online' in query:

            webbrowser.open("https://www.amazon.com")

            speak("opening amazon")

            print("opening amazon")

        elif 'open flipkart' in query:

            webbrowser.open("https://www.flipkart.com")

            speak("opening flipkart")

            print("opening flipkart")

        elif 'open ebay' in query:

            webbrowser.open("https://www.ebay.com")

            speak("opening ebay")

            print("opening ebay")

        elif 'open notepad' in query:

            speak('opening notepad..')
            print('opening notepad..')
            os.system('notepad')

        elif 'open command prompt' in query:

            speak('opening CMD..')

            print('opening CMD..')
            os.system('start')

        elif 'open this pc' in query or 'open my computer' in query:

            speak('opening this pc..')

            print('opening this pc..')

            os.chdir('c:\\')


        elif 'create a folder' in query:

            speak('creating new folder')

            print('creating new folder')

            os.chdir('C:\\Users\\Payal\\Desktop')

            os.system('md new_folder')

        elif 'this pc' in query or 'my pc' in query:

            speak('opening this pc..')

            print('opening this pc..')

            os.system('Explorer')


        elif 'what is date today' in query or 'date' in query:

            speak('today date..')
            print('today date..')

            datetime_object = datetime.datetime.now()

            print(datetime_object)

            speak(datetime_object)


        elif 'music from pc' in query or "music" in query:

            speak("ok i am playing music")

            print("ok i am playing music")

            music_dir = './music'

            musics = os.listdir(music_dir)

            os.startfile(os.path.join(music_dir, musics[0]))

        elif 'video from pc' in query or "video" in query:

            speak("ok i am playing videos")

            video_dir = './video'

            videos = os.listdir(video_dir)

            os.startfile(os.path.join(video_dir, videos[0]))

        elif 'good bye' in query:

            speak("good bye")

            print("good bye")

            exit()

        elif 'send email' in query:

            speak('Who is the recipient? ')

            print('Who is the recipient? ')

            recipient = takecom()


            if 'my self' in recipient:


             try:

                    speak('What should I say? ')

                    print('What should I say? ')

                    content = takecom()


                    server = smtplib.SMTP('smtp.gmail.com', 587)

                    server.ehlo()

                    server.starttls()

                    server.login("YOUSER EMAIL", 'PASSWARD')

                    server.sendmail('USER NAME', "RECIPITANE", content)

                    server.close()

                    speak('Email sent!')

                    print('Email sent!')


             except:

                    speak('Sorry Sir! I am unable to send your message at this moment!')

                    print('Sorry Sir! I am unable to send your message at this moment!')

        elif "shutdown" in query:

            speak("shutting down")

            print("shutting down")

            os.system('shutdown -s')


        elif "what\'s up" in query or 'how are you' in query:

            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy',

                      'i am okey ! How are you']

            ans_q = random.choice(stMsgs)

            speak(ans_q)

            print(ans_q)

            ans_take_from_user_how_are_you = takecom()

            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:

                speak('okey..')

                print('okey..')

            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:

                speak('oh sorry..')

                print('oh sorry..')

        elif 'make you' in query or 'created you' in query or 'develop you' in query:

            ans_m = " For your information YOU Created me ! I give Lot of Thannks to Him "

            print(ans_m)

            speak(ans_m)

        elif "who are you" in query or "about you" in query or "your details" in query:

            about = "I am alais an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "

            print(about)

            speak(about)

        elif "hello" in query or "hello alais" in query:

            hel = "Hello SIR ! How May i Help you.."

            print(hel)

            speak(hel)

        elif "your name" in query or "sweat name" in query:

            na_me = "Thanks for Asking my name my self ! alais"

            print(na_me)

            speak(na_me)

        elif "you feeling" in query:

            print("feeling Very sweet after meeting with you")

            speak("feeling Very sweet after meeting with you")

        elif query == 'none':
            continue

        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query:

            ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'

            speak(ex_exit)

            print(ex_exit)

            exit()

        else:

            query = query

            speak('Searching...')

            print('searching...')

            try:

                try:

                    res = client.query(query)

                    results = next(res.results).text

                    speak('WOLFRAM-ALPHA says - ')

                    print('WOLFRAM-ALPHA says - ')

                    speak('Got it.')

                    print('Got it.')

                    speak(results)
                    print(results)


                except:

                    results = wikipedia.summary(query, sentences=2)

                    speak('Got it.')

                    print('Got it.')

                    speak('WIKIPEDIA says - ')

                    print('WIKIPEDIA says - ')

                    speak(results)
                    print(results)


            except:

                webbrowser.open('www.google.com')



