from Tone import Tone

speed = int(input("Please chose WPM speed:\n"))
value = input("Please enter a letter:\n")

# Speed calculation at 1 WPM
di = Tone.sine(750, duration=1.2/speed)
dah = Tone.sine(750, duration=3.6/speed)
intra_char = Tone.sine(0, duration=1.2/speed)
inter_char = Tone.sine(0, duration=3.6/speed)
intra_word = Tone.sine(0, duration=8.4/speed)

v1 = str(value)

if v1 == 'a':
    Tone.sine(750, duration=di)   # di
    Tone.sine(0, duration=intra_char)     # intra-char
    Tone.sine(750, duration=dah)   # da
elif v1 == 'b':
    Tone.sine(750, duration=0.18)   # da
    Tone.sine(0, duration=0.06)     # intra-char
    Tone.sine(750, duration=0.06)   # di
    Tone.sine(0, duration=0.06)     # intra-char
    Tone.sine(750, duration=0.06)   # di
    Tone.sine(0, duration=0.06)     # intra-char
    Tone.sine(750, duration=0.06)   # di
elif v1 == 'c':
    Tone.sine(750, duration=0.18)   # da
    Tone.sine(0, duration=0.06)     # intra-char
    Tone.sine(750, duration=0.06)   # di
    Tone.sine(0, duration=0.06)     # intra-char
    Tone.sine(750, duration=0.18)   # da
    Tone.sine(0, duration=0.06)     # intra-char
    Tone.sine(750, duration=0.06)   # di





# # The below PARIS test word is sent a 20 WPM
# # This is the letter 'P'
# Tone.sine(750, duration=0.06)   # di
# Tone.sine(0, duration=0.06)     # intra-char
# Tone.sine(750, duration=0.18)   # da
# Tone.sine(0, duration=0.06)     # intra-char
# Tone.sine(750, duration=0.18)   # da
# Tone.sine(0, duration=0.06)     # intra-char
# Tone.sine(750, duration=0.06)   # di
# Tone.sine(0, duration=0.18)     # intra-char

# # This is the letter 'A'
# Tone.sine(750, duration=0.06)   # di
# Tone.sine(0, duration=0.06)     # intra-chara
# Tone.sine(750, duration=0.18)   # da
# Tone.sine(0, duration=0.18)     # intra-char

# # This is the letter 'R'
# Tone.sine(750, duration=0.06)   # di
# Tone.sine(0, duration=0.06)     # intra-char
# Tone.sine(750, duration=0.18)   # da
# Tone.sine(0, duration=0.06)     # intra-char
# Tone.sine(750, duration=0.06)   # di
# Tone.sine(0, duration=0.18)     # intra-char

# # This is the letter 'I'
# Tone.sine(750, duration=0.06)   # di
# Tone.sine(0, duration=0.06)     # intra-char
# Tone.sine(750, duration=0.06)   # di
# Tone.sine(0, duration=0.18)     # intra-char

# # This is the letter 'S'
# Tone.sine(750, duration=0.06)   # di
# Tone.sine(0, duration=0.06)     # intra-char
# Tone.sine(750, duration=0.06)   # di
# Tone.sine(0, duration=0.06)     # intra-char
# Tone.sine(750, duration=0.06)   # di
# Tone.sine(0, duration=0.42)     # intra-word