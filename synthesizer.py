from helper import *
import speech_recognition as sr
from time import sleep

r = sr.Recognizer()
m = sr.Microphone()

volume = 5
octave = 1
tempo = 120

def synthesizer():
	melody = ""
	while(True):
	   try:
	       with m as source: r.adjust_for_ambient_noise(source)
	       print("Say a series of notes A - G")
	       with m as source: audio = r.listen(source)
	       try:
	           value = r.recognize_google(audio)
	           show_progress()
	           melody = "{}".format(value)
	           #print("raw: " + melody)
	       except sr.UnknownValueError:
	       	show_progress()
	       	print("Didn't hear you properly.")
	       except sr.RequestError as e:
	       	show_progress()
	       	print("Error")
	   except KeyboardInterrupt:
	       pass
	       break

	   if(verify(melody)):
	   	return melody
	   	break
	   else:
	   	if(melody != None):
	         print("You said '" + melody + "'. Make sure you say a series of notes A through G!")
	         sleep(0.5)
	   	else:
	         print("Make sure you say a series of notes A through G!")

	   spacer()
