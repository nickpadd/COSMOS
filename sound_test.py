global volume
volume = 4

def noise(frequency, duration = 2.0, octave = 4):
    import pyaudio
    import numpy as np

    p = pyaudio.PyAudio()

    v = volume / 10
    fs = 44100
    d = duration * 4

    if(octave == 4):
        f = frequency
    elif(octave == 3):
        f = frequency / 2
    elif(octave == 5):
        f = frequency * 2
    elif(octave == 6):
        f = frequency * 4

    samples = (np.sin(2*np.pi*np.arange(fs*d)*f/fs)).astype(np.float32)

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    #visual(f) #MAKE SURE TO RE-ENABLE LATER
    stream.write(v*samples)

    # stream.stop_stream()
    # stream.close()

    # p.terminate()

noise(440, 2, 4)
#divide by 4?