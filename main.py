from tuner import *
from synthesizer import *
from switch import *
from helper import *

def start():

    while(True):
        spacer()
        type = switch()

        if(type == "tuner"):
            noise_tuner(parse_tuner_frequency(tuner()))

        elif(type == "synthesizer"):
            sound(parse_input(synthesizer()))

        elif(type == "settings"):
            cont = parse_settings(do_settings())
            while(cont):
                cont = parse_settings(do_settings())

        elif(type == "quit"):
            print("Exiting...")
            sleep(0.75)
            quit()

start()
