from Tone import Tone
import random

# some constants
WPS = 15            # 15 words per minute default
DI = 1.2/WPS        # gaps dependent on wps
DAH = 3 * DI        # dashes are 3 times longer
INTRA_CHAR = DI     # gap between dots and dashes
INTER_CHAR = 3 * DI # gap between letters
INTRA_WORD = 7 * DI # gap between words

FREQUENCY = 780     # default pitch of dots and dashes
SILENCE = 0         # value of silence

# the full morse code alphabet
ALPHABET = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----."
        }

# create a silent gap between letters
def silent_gap_between_letters():
    Tone.sine(SILENCE, INTER_CHAR)

# create a silent gap between words
def silent_gap_between_words():
    Tone.sine(SILENCE, INTRA_WORD)

# Play the morse code representation of the letter we ask to hear
# from the alphabet we're using
def sound_letter(c : str, alpha : dict):
    character = alpha.get(c)
    for i in character:
        if i == '.':        # if we have a di
            Tone.sine(FREQUENCY, DI)
        else:               # else we must have dah
            Tone.sine(FREQUENCY, DAH)

        # print an appropriate gap
        Tone.sine(SILENCE, INTRA_CHAR)

# Return a copy of the full alphabet containng n letters
def new_dictionary(n : int) -> dict:
    a = dict()
    for x in range(n):
        a[list(ALPHABET.keys())[x]] = list(ALPHABET.values())[x]
    return a

# Return a list of a random sequence of n letters from the current alphabet
def rand_sequence(n : int, alpha : dict) -> list:
    L = []
    for _ in range(n):
        L.append(random.randrange(len(alpha)))
    X = list(alpha.keys())
    return [X[i] for i in L]

# main code starts here
if __name__ == "__main__":

    # kick off our random number generator
    random.seed(17)

    # start with a small alphabet
    alphabet_length = 3
    print('Using an alphabet of the first', alphabet_length, 'characters')

    alpha = new_dictionary(alphabet_length)
    print(alpha)

    # sound the given letters in our alphabet
    for x in alpha:
        sound_letter(x, alpha)
        silent_gap_between_letters()

    print('Generating 5 random sequences of 5 letters each from our alphabet')

    for _ in range(5):
        L = rand_sequence(5, alpha)
        print(L)
        for c in L:
            sound_letter(c, alpha)
            silent_gap_between_letters()

        silent_gap_between_words()
