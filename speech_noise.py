#!/usr/bin/python3

import speech_recognition as sr

print("Using version ", sr.__version__)

r = sr.Recognizer()

## read .wav file
harvard = sr.AudioFile('jackhammer.wav')
with harvard as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)

print("type is ", type(audio))

print("result is ", r.recognize_google(audio, show_all=True))
