from bar import *

keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
values = [440.0, 494.0, 523.0, 587.0, 659.0, 698.0, 784.0]
dictionary = dict(zip(keys,values))

#################################
########## S W I T C H ##########
#################################

def show_progress():
    from time import sleep

    items = list(range(0, 57))
    l = len(items)

    progress_bar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i, item in enumerate(items):
        sleep(0.015)
        progress_bar(i + 1, l, prefix = 'Processing:', suffix = 'Complete', length = 50)

def check_valid(function):
    if(function.lower() == "tuner"):
        return True
    elif(function.lower() == "synthesizer"):
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

def ask_octave():
    print("hi")

def ask_tempo():
    print("hi")

def check_valid_note(note):
    if(isinstance(note, str)):
        if(len(note) == 1):
            return True
    else:
        return False

def noise(frequency, volume = 1.0, duration = 10.0):
    import pyaudio
    import numpy as np

    p = pyaudio.PyAudio()

    v = volume
    fs = 44100
    d = duration
    f = frequency

    samples = (np.sin(2*np.pi*np.arange(fs*d)*f/fs)).astype(np.float32)

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    visual(f)
    stream.write(v*samples)

    stream.stop_stream()
    stream.close()

    p.terminate()

def visual(frequency):
    note = dictionary.get(frequency)
    #do something
    #hook to arduno

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
    print(melody)
    return melody

def sound(melody):
    for note in melody:
        noise(parse_tuner_frequency(note), 1.0, 1.5)

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
    for i in range(1,20):
        print("")
