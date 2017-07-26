from helper import *
from bar import *
import speech_recognition as sr
from time import sleep

r = sr.Recognizer()
m = sr.Microphone()

volume = 5
octave = 1

def tuner():
	note = ""
	while(True):
	   try:
	       with m as source: r.adjust_for_ambient_noise(source)
	       print("Say a note A - G")
	       with m as source: audio = r.listen(source)
	       try:
	           value = r.recognize_google(audio)
	           show_progress()
	           note = "{}".format(value)
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

	   note = correct_pronunciation(note)

	   if(parse_type(note) == "note"):
	       if(correct_pronunciation(note) != False):
	           return correct_pronunciation(note)
	           break
	   elif(parse_type(note) == "command"):
	       parse_command(note)
	   else:
	   	if(note != None):
	         print("You said '" + note + "'. Make sure you say a note A through G!")
	         sleep(0.5)
	   	else:
	         print("Make sure you say a note A through G!")

	   spacer()
