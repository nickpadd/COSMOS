global volume
volume = 5

def noise(frequency, duration = 2.0):
    import pyaudio
    import numpy as np

    p = pyaudio.PyAudio()

    v = volume / 10
    fs = 44100
    d = duration * 4
    f = frequency

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

noise(440, 2)
#divide by 4?