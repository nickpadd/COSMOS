import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

def test():
	option = ""
	while(True):
	   try:
	       with m as source: r.adjust_for_ambient_noise(source)
	       print("Speak")
	       with m as source: audio = r.listen(source)
	       try:
	           value = r.recognize_google(audio)
	           option = "{}".format(value)
	           print(option)
	       except sr.UnknownValueError:
	       	print("Didn't hear you properly.")
	       except sr.RequestError as e:
	       	print("Error")
	   except KeyboardInterrupt:
	       pass
	       break

test()