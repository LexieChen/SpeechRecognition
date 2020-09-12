#!/usr/bin/python3

import speech_recognition as sr

print("Using version ", sr.__version__)

r = sr.Recognizer()

## read audio from mic
mic = sr.Microphone()
#print("mics ", sr.Microphone.list_microphone_names())

with mic as source:
    audio = r.listen(source)

print("result is ", r.recognize_google(audio))
