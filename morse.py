# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sounddevice as sd
import numpy as np
from math import pi

# Sampling Frequency
Fs = 16000

# Define time axis
n = np.arange(0,0.1,1/Fs)     # numpy.arange([start, ] stop, [step, ]dtype=None, *, like=none)
f = 1000;

x = np.sin(2*pi*f*n)

# Play sound
sd.play(x, Fs)
