from time import sleep
import speech_recognition as sr

#Settings
global volume #max 10
global octave #2-6
global tempo #30-180

volume = 5
octave = 4
tempo = 120

r = sr.Recognizer()
m = sr.Microphone()

def initial_check():
	option = ""
	while(True):
	   try:
	       with m as source: r.adjust_for_ambient_noise(source)
	       print("Would you like to change these settings?")
	       with m as source: audio = r.listen(source)
	       try:
	           value = r.recognize_google(audio)
	           show_progress()
	           option = "{}".format(value)
	       except sr.UnknownValueError:
	       	show_progress()
	       	print("Didn't hear you properly.")
	       except sr.RequestError as e:
	       	show_progress()
	       	print("Error")
	   except KeyboardInterrupt:
	       pass
	       break

	   if(check_legit(option)[0]):
	      return check_legit(option)[1]
	   else:
	       print("You said '" + option + "'. Make sure you say either yes or no!")
	       sleep(1.5)

	   spacer()

def settings():
	option = ""
	while(True):
	   try:
	       with m as source: r.adjust_for_ambient_noise(source)
	       print("Say the setting you would like to change, followed by a number. If the number is two more digits, say each digit.")
	       print("Example: 'tempo 1 1 4' or 'volume 7'")
	       print("NOTE: max volume is 10, octave range from 2-6, tempo range is 30-180")
	       print("")
	       #sleep(2)
	       print("Speak now")
	       sleep(0.5)
	       with m as source: audio = r.listen(source)
	       try:
	           value = r.recognize_google(audio)
	           show_progress()
	           option = "{}".format(value)
	       except sr.UnknownValueError:
	       	show_progress()
	       	print("Didn't hear you properly.")
	       except sr.RequestError as e:
	       	show_progress()
	       	print("Error")
	   except KeyboardInterrupt:
	       pass
	       break

	   if(len(option) > 0):
	   	if(check_settings_legit(option)):
	   		return option
	   	else:
	   		print("You said '" + option + "'. Make sure you said the right thing!")
	   		sleep(1.5)

	   spacer()
##
from bar import *
from time import sleep

def show_settings():
    print("          Current settings          ")
    print("––––––––––––––––––––––––––––––––––––")
    print("Volume: " + str(volume) + "/10")
    print("Tempo: " + str(tempo) + " bpm")
    print("Octave: " + str(octave) + " (default 4)")
    print("")
    sleep(1.5)

def show_progress():

    items = list(range(0, 57))
    l = len(items)

    progress_bar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i, item in enumerate(items):
        sleep(0.015)
        progress_bar(i + 1, l, prefix = 'Processing:', suffix = 'Complete', length = 50)
    spacer()

def spacer():
    for i in range(1,100):
        print("")

#THIS METHOD COMES FIRST
def do_settings():
    show_settings()
    if(initial_check()):
        return settings()
    else:
        print("Okay, returning...")
        sleep(1)

def check_legit(option):
	if(option == "yes"):
		return True, True
	elif(option == "no"):
 		return True, False
	else:
 		return False, False

def check_settings_legit(setting):
    parsed = setting.split()

    parsed[0] = correct_setting(parsed[0])

    if(parsed[0] == "tempo"):
        #ADD NUMBER CHECK
        return True
    elif(parsed[0] == "volume"):
        return True
    elif(parsed[0] == "octave"):
        return True
    else:
        return False

def parse_settings(setting):
    if(setting == None):
    	return False
    parsed = setting.split()
    if(parsed[0].lower() == "tempo"):
        change_tempo(parsed)
        return True
    elif(parsed[0].lower() == "volume"):
        change_volume(parsed)
        return True
    elif(parsed[0].lower() == "octave"):
        change_octave(parse)
        return True
    else:
        return False

def correct_setting(setting):
    return setting.lower()

def change_tempo(setting):
    if(len(setting) == 2):
        if((int(correct_number(setting[1])) >= 30) and (int(correct_number(setting[1])) <= 180)):
            global tempo
            tempo = int(correct_number(setting[1]) + correct_number(setting[2]))
        else:
            print("Min tempo is 30!")
    elif(len(setting) == 3):
        if(int(correct_number(setting[1]) + correct_number(setting[2])) >= 30):
            tempo = int(correct_number(setting[1]) + correct_number(setting[2]))
        else:
            print("Min tempo is 30!")
    elif(len(setting) == 4):
        if(correct_number(int(setting[1]) + correct_number(setting[2]) + correct_number(setting[3])) <= 180):
            tempo = int(correct_number(setting[1]) + correct_number(setting[2]) + correct_number(setting[3]))
        else:
            print("Max tempo is 180!")

def change_octave(setting):
    if(len(setting) == 2):
        if((int(correct_number(setting[1])) >= 2) and (int(correct_number(setting[1])) <= 6)):
            global octave
            octave = int(correct_number(setting[1]) + correct_number(setting[2]))
        else:
            print("Min octave is 2 and max octave is 6!")

def change_volume(setting):
	if(len(setting) == 2):
		global volume
		volume = int(correct_number(setting[1]))
	elif(len(setting) == 3):
		if(int(correct_number(setting[1]) + correct_number(setting[2])) == 10):
			#global volume
			volume = int(correct_number(setting[1]) + correct_number(setting[2]))
		else:
			print("Max volume is 10!")

def correct_number(input):
	if(input == "one"):
		return "1"
	elif(input == "two"):
		return "2"
	elif(input == "three"):
		return "3"
	elif(input == "four"):
		return "4"
	elif(input == "five"):
		return "5"
	elif(input == "six"):
		return "6"
	elif(input == "seven"):
		return "7"
	elif(input == "eight"):
		return "8"
	elif(input == "nine"):
		return "9"
	elif(input == "zero"):
		return "0"
	else:
		return input
