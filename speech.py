#!/usr/bin/python3

import speech_recognition as sr

print("Using version ", sr.__version__)

r = sr.Recognizer()

## read .wav file
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source, duration=3, offset=4)

print("type is ", type(audio))

print("result is ", r.recognize_google(audio))
