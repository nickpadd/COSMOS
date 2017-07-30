from bar import *
from visual import *
from time import sleep
#from light import * RE-ENABLE ON JUN'S LAPTOP

keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
values = [440.0, 494.0, 523.0, 587.0, 659.0, 698.0, 784.0]
dictionary = dict(zip(keys,values))
dictionary2 = dict(zip(values,keys))

#################################
######## S E T T I N G S ########
#################################

import speech_recognition as sr

#Settings
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
	       sleep(1)
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

from bar import *
from time import sleep

def show_settings():
    print("          Current settings          ")
    print("––––––––––––––––––––––––––––––––––––")
    print("Volume: " + str(volume) + "/10")
    print("Tempo: " + str(tempo) + " bpm")
    print("Octave: " + str(octave) + " (default 4)")
    print("")
    sleep(1.0)

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
        change_octave(parsed)
        return True
    else:
        return False

def correct_setting(setting):
    return setting.lower()

def change_tempo(setting):
    global tempo
    if(len(setting) == 2):
        if((int(correct_number(setting[1])) >= 30) and (int(correct_number(setting[1])) <= 180)):
            tempo = int(correct_number(setting[1]))
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
    global octave
    if(len(setting) == 2):
        if((int(correct_number(setting[1])) >= 3) and (int(correct_number(setting[1])) <= 6)):
            octave = int(correct_number(setting[1]))
        else:
            print("Min octave is 3 and max octave is 6!")

def change_volume(setting):
	global volume
	if(len(setting) == 2):
		volume = int(correct_number(setting[1]))
	elif(len(setting) == 3):
		if(int(correct_number(setting[1]) + correct_number(setting[2])) == 10):
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

#################################
########## S W I T C H ##########
#################################

def show_progress():

    items = list(range(0, 57))
    l = len(items)

    progress_bar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i, item in enumerate(items):
        sleep(0.012)
        progress_bar(i + 1, l, prefix = 'Processing:', suffix = 'Complete', length = 50)
    spacer()

def check_valid(function):
    if(function.lower() == "tuner"):
        return True
    elif(function.lower() == "synthesizer"):
        return True
    elif(function.lower() == "settings"):
        return True
    elif(function.lower() == "quit"):
        return True
    else:
        return False

#################################
########### T U N E R ###########
#################################

def parse_type(word):
    if(check_valid_note(word)):
        if(len(word) == 1):
            return "note"
        elif(len(word) > 1):
            return "command"

def parse_command(word):
    if(word.lower() == "octave"):
        get_octave
    elif(word.lower() == "tempo"):
        get_tempo

def correct_pronunciation(note):
    if(note == "see"):
        note = "c"
    elif(note == "B"):
        note = "b"
    elif(note == "G"):
        note = "g"
    elif(note == "hey"):
        note = "a"
    elif(note == "she"):
        note = "c"
    elif(note == "gee"):
        note = "g"
    elif(note == "bee"):
        note = "b"
    elif(note == "T"):
        note = "e"
    elif(note == "tea"):
        note = "e"

    if(check_valid_note(note)):
        if((ord(note) in range (ord('a'), ord('h')) or ord(note) in range (ord('A'), ord('H')))):
            return note.lower()
        else:
            return False

def check_valid_note(note):
    if(isinstance(note, str)):
        if(len(note) == 1):
            return True
    else:
        return False

def noise_tuner(frequency):
    import pyaudio
    import numpy as np

    p = pyaudio.PyAudio()

    v = volume / 10
    fs = 44100
    d = 8.0

    if(octave == 4):
        f = frequency
    elif(octave == 3):
        f = frequency / 2
    elif(octave == 5):
        f = frequency * 2
    elif(octave == 6):
        f = frequency * 4

    terminal_display(dictionary2.get(frequency))

    samples = (np.sin(2*np.pi*np.arange(fs*d)*f/fs)).astype(np.float32)

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    #visual(f) #MAKE SURE TO RE-ENABLE LATER
    stream.write(v*samples)

    stream.stop_stream()
    stream.close()

    p.terminate()

def visual(frequency):
    note = dictionary2.get(frequency)
    make_light(note)

def parse_tuner_frequency(note):
    return dictionary.get(note)

#################################
##### S Y N T H E S I Z E R #####
#################################

def parse_input(melody):
    melody = list(melody)
    for index,note in enumerate(melody):
        if(note == " "):
            del melody[index]
    for note in melody:
        note = correct_pronunciation(note)
    for index,note in enumerate(melody):
        melody[index] = melody[index].lower()
    return melody

def noise_synth(frequency):
    import pyaudio
    import numpy as np

    p = pyaudio.PyAudio()

    v = volume / 10
    fs = 44100
    d = (60 / tempo) * 4

    if(octave == 4):
        f = frequency
    elif(octave == 3):
        f = frequency / 2
    elif(octave == 5):
        f = frequency * 2
    elif(octave == 6):
        f = frequency * 4

    terminal_display(dictionary2.get(f))

    samples = (np.sin(2*np.pi*np.arange(fs*d)*f/fs)).astype(np.float32)

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    #visual(f) #MAKE SURE TO RE-ENABLE LATER
    stream.write(v*samples)

    stream.stop_stream()
    stream.close()

    p.terminate()

def sound(melody):
    for note in melody:
        spacer()
        noise_synth(parse_tuner_frequency(note))

def verify(melody):
    good = True
    melody = list(melody)
    for index,note in enumerate(melody):
        if(note == " "):
            del melody[index]
    for note in melody:
        if(correct_pronunciation(note) == False):
            return False
        elif((ord(correct_pronunciation(note)) in range (ord('a'), ord('h')) or ord(correct_pronunciation(note)) in range (ord('A'), ord('H')))):
            print()
        else:
            return False
            break
    return True

#################################
############ M I S C ############
#################################

def spacer():
    for i in range(1,100):
        print("")

def terminal_display(note):
    if(note == "a"):
        print(A(), end = "\r", flush = True)
    if(note == "b"):
        print(B(), end = "\r", flush = True)
    if(note == "c"):
        print(C(), end = "\r", flush = True)
    if(note == "d"):
        print(D(), end = "\r", flush = True)
    if(note == "e"):
        print(E(), end = "\r", flush = True)
    if(note == "f"):
        print(F(), end = "\r", flush = True)
    if(note == "g"):
        print(G(), end = "\r", flush = True)
