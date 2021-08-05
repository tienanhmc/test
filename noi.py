import pyttsx3

word = "all my friends are dead"

engine = pyttsx3.init()
engine.say(word)
engine.runAndWait()