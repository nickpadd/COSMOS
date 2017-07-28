from helper import *
import speech_recognition as sr
from bar import *

r = sr.Recognizer()
m = sr.Microphone()

def test():
	option = ""
	while(True):
	   try:
	       with m as source: r.adjust_for_ambient_noise(source)
	       print("Say something.")
	       with m as source: audio = r.listen(source)
	       try:
	           value = r.recognize_google(audio)
	           show_progress()
	           option = "{}".format(value)
	           print(option)
	       except sr.UnknownValueError:
	       	show_progress()
	       	print("Didn't hear you properly.")
	       except sr.RequestError as e:
	       	show_progress()
	       	print("Error")
	   except KeyboardInterrupt:
	       pass
	       break

test()
