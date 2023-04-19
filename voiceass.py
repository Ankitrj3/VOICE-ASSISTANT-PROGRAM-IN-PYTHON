import speech_recognition as sr
import pyttsx3
import webbrowser

# initialize the speech recognition engine and text-to-speech engine
liki = sr.Recognizer()
engine = pyttsx3.init()

# define a function to speak the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# define a function to perform a Google search
def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak("Here are the search results for " + query)

# start the voice assistant program
with sr.Microphone() as source:
    speak("how i can help you")
    while True:
        # listen for audio input
        audio = liki.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            query = liki.recognize_google(audio)
            print("User:", query)

            # check for exit command
            if "exit" in query:
                speak("Goodbye")
                break

            # perform a Google search for the query
            search_google(query)

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
