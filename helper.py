from light import *
from bar import *
from visual import *
from settings import *
from time import sleep

#Frequency reference
keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
values = [440.0, 494.0, 523.0, 587.0, 659.0, 698.0, 784.0]
dictionary = dict(zip(keys,values))
dictionary2 = dict(zip(values,keys))

#################################
########## S W I T C H ##########
#################################

def show_progress():

    items = list(range(0, 57))
    l = len(items)

    progress_bar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i, item in enumerate(items):
        sleep(0.015)
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

#Default 2 seconds
def noise(frequency = 440, duration = 2.0):
    import pyaudio
    import numpy as np

    p = pyaudio.PyAudio()

    #DIVIDE DURATION BY 4 (SECONDS)

    v = volume / 10
    fs = 44100
    d = (60 / tempo) * 4
    f = frequency

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

def sound(melody):
    for note in melody:
        spacer()
        noise(parse_tuner_frequency(note), 1.5)

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
######## S E T T I N G S ########
#################################

#moved to settings_helper.py

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
