import speech_recognition as sr
import pyttsx3
from pyChatGPT import ChatGPT
from chatgpt import chat
# Initialize the recognizer
r = sr.Recognizer()
# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


try:
    with sr.Microphone() as source2:
        r.energy_threshold = 3000
        r.adjust_for_ambient_noise(source2, duration=0.2)
        print("Say Something")
        audio2 = r.listen(source2)
        MyText = r.recognize_google(audio2)
        print("Listened you")
        MyText = MyText.lower()
        bot_answer = chat(MyText)
        SpeakText(bot_answer)
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

except sr.UnknownValueError:
    print("unknown error occurred")