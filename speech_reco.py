import speech_recognition as sr
import pyttsx3
from googlesearch import search

# Initialize speech recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()


# Define a function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Define a function to listen for speech and return the recognized text
def listen():
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            print("Sorry, I did not understand that.")
            return ""


# Main program loop
while True:
    # Get user input
    command = listen()

    # If the user said something, process the command
    if command != "":
        print("You said: " + command)
        

        # Here you can add your own logic to interpret the user's command and take appropriate action
        # For example, you could use a series of if/elif statements to check for specific keywords

        # Respond to the user
        response = "I heard you say " + command
        speak(response)
