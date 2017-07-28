from helper import *
import speech_recognition as sr
from time import sleep

r = sr.Recognizer()
m = sr.Microphone()

def switch():
	function = ""
	while(True):
	   try:
	       with m as source: r.adjust_for_ambient_noise(source)
	       print("Tuner, synthesizer, settings, or quit?")
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
	       print("You said '" + function + ".' Make sure you say either tuner, synthesizer, or settings!")
	       sleep(1.5)

	   spacer()
