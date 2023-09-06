import speech_recognition as sr
from speak import talk
def listen():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            talk("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source,0,5)
            talk("Recognizing....")
            query = r.recognize_google(audio,language="en-in")
            print(f"User said : {query}")
            query = str(query)
            return query.lower()
    except Exception as w:
        print(w)
        talk("Say that again please...")