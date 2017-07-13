#using predefined Google API for Speech Recognition 
import speech_recognition as sr
 
# Record Audio

r = sr.Recognizer()     #recognize the pcm cards 
with sr.Microphone() as source:
    print("Please say a few words")
    audio = r.listen(source)
try:
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("not getting the results ")
except sr.RequestError as e:
    print("network error {0}".format(e))
