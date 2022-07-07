import speech_recognition as sr


def command_word(text):
    if text.lower() == "start":
        print(">>> Start command activated")
    elif text.lower() == "next":
        print(">>> Next command activated")
    elif text.lower() == "undo":
        print(">>> Undo command activated")
    else:
        print("not a command")


r = sr.Recognizer()

# print(sr.Microphone.list_microphone_names())

with sr.Microphone() as source:
    
    r.adjust_for_ambient_noise(source,duration=1)
    print("Say stuff...")

    while(True):
        audio_text = r.listen(source)
        
        # recoginize_() method will throw a request error if the API is unreachable
        # hence using exception handling
        try:
            # using google speech recognition
            text = r.recognize_google(audio_text)
            print(text)
            command_word(text)
        
        except Exception:
            print('Sorry, didn\'t catch that')
