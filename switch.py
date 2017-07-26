from helper import *
import speech_recognition as sr
from time import sleep
import music21

r = sr.Recognizer()
m = sr.Microphone()

def switch():
	function = ""
	while(True):
	   try:
	       with m as source: r.adjust_for_ambient_noise(source)
	       print("Do you want to use the tuner or the synthesizer?")
	       with m as source: audio = r.listen(source)
	       try:
	           value = r.recognize_google(audio)
	           show_progress()
	           function = "{}".format(value)
	       except sr.UnknownValueError:
	       	show_progress()
	       	print("Didn't hear you properly.")
	       except sr.RequestError as e:
	       	show_progress()
	       	print("Error")
	   except KeyboardInterrupt:
	       pass
	       break

	   if(check_valid(function)):
	       return function
	       break
	   else:
	       print("You said '" + function + ".' Make sure you say either tuner or synthesizer!")
	       sleep(0.5)

	   spacer()
