from tuner import *
from synthesizer import *
from switch import *
from helper import *

def start():
    type = switch()
    #type = "synthesizer"
    if(type == "tuner"):
        noise(parse_tuner_frequency(tuner()))

    elif(type == "synthesizer"):
        sound(parse_input(synthesizer()))

    #while true for entire thing
    #surround the if else statement
    #run either the tuner or synthesizer until something becomes False
    #check for voice input every time it loops

start()
