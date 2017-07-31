from helper import *
import speech_recognition as sr
from time import sleep

r = sr.Recognizer()
m = sr.Microphone()

def triad():
	base = ""
	while(True):
	   try:
	       with m as source: r.adjust_for_ambient_noise(source)
	       print("Say a note A - G (this is the root note)")
	       with m as source: audio = r.listen(source)
	       try:
	           value = r.recognize_google(audio)
	           show_progress()
	           base = "{}".format(value)
	       except sr.UnknownValueError:
	       	show_progress()
	       	print("Didn't hear you properly.")
	       except sr.RequestError as e:
	       	show_progress()
	       	print("Error")
	   except KeyboardInterrupt:
	       pass
	       break

	   base = correct_pronunciation(base)

	   if(parse_type(base) == "note"):
	       if(correct_pronunciation(base) != False):
	           return correct_pronunciation(base)
	           break
	   # elif(parse_type(note) == "command"):
	   #     parse_command(note)
	   else:
	   	if(base != None):
	   		if(base != True):
	   			if(base != False):
			         print("You said '" + base + "'. Make sure you say a note A through G!")
			         sleep(1.5)
	   	else:
	         print("Make sure you say a note A through G!")
	         sleep(1.5)

	   spacer()
