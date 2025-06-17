import pywhatkit
import pyttsx3
import speech_recognition as sr
import datetime
import time

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, I didn't catch that.")
        return ""

def send_whatsapp_message(phone_no, message):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 2  # Delay of 2 minutes
    pywhatkit.sendwhatmsg(phone_no, message, hour, minute)
    speak("WhatsApp message scheduled successfully.")

def run_jarvis():
    while True:
        speak("Say 'Jarvis' to activate.")
        wake_word = listen()
        if "jarvis" in wake_word:
            speak("Yes, I'm listening. What do you want to do?")
            command = listen()

            if "whatsapp" in command:
                speak("Whom do you want to message? Please say the phone number with country code.")
                phone = listen()
                phone = phone.replace(" ", "").replace("+", "")
                if not phone.startswith("91"):  # For Indian numbers
                    phone = "91" + phone

                phone = "+" + phone
                speak("What is the message?")
                msg = listen()
                send_whatsapp_message(phone, msg)

            elif "stop" in command:
                speak("Goodbye!")
                break
            else:
                speak("I didn't understand. Try again.")

run_jarvis()