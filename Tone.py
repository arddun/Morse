# Sine Wave formula from https://en.wikipedia.org/wiki/Sine_wave
# Tutorial from Jammin' Coder - Generating Sound from Sine Waves in Python - YouTube

# Install pygame and numpy with "pip3 install xxxxx"

import pygame
import numpy
import math
import time

pygame.init()

bits = 16
sample_rate = 44100

pygame.mixer.pre_init(sample_rate, bits)

def sine_x(amp, freq, time):
    return int(round(amp * math.sin(2 * math.pi * freq * time)))    #Sine Wave formula


class Tone:
    def sine(freq, duration=1, speaker=None):
        
        num_samples = int(round(duration * sample_rate))

        sound_buffer = numpy.zeros((num_samples, 2), dtype = numpy.int16)
        amplitude = 2 ** (bits - 1) - 1

        for sample_num in range(num_samples):
            t = float(sample_num) / sample_rate

            sine = sine_x(amplitude, freq, t)

            if speaker == 'r':
                sound_buffer[sample_num][1] = sine
            if speaker == 'l':
                sound_buffer[sample_num][0] = sine
            else:
                sound_buffer[sample_num][1] = sine
                sound_buffer[sample_num][0] = sine

        sound = pygame.sndarray.make_sound(sound_buffer)
        sound.play(loops=1, maxtime=int(duration * 1000))
        time.sleep(duration)
