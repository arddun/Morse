from Tone import Tone

# some constants
wps = 15            # 15 words per minute default
di = 1.2/wps        # gaps dependent on wps
dah = 3 * di        # dashes are 3 times longer
intra_char = di     # gap between dots and dashes
inter_char = 3 * di # gap between letters
intra_word = 7 * di # gap between words

# the full morse code alphabet
alphabet = {
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

# Play the morse code representation of the letter we ask to hear
# from the alphabet we're using
def sound_letter(c : str, alpha : dict):
    character = alpha.get(c)
    for i in character:
        if i == '.':        # if we have a di
            Tone.sine(750,di)
        else:               # else we must have dah
            Tone.sine(750,dah)

        # print an appropriate gap
        Tone.sine(0, intra_char)

# Create a copy of the full alphabet containng n letters
def new_dictionary(n : int) -> dict:
    a = dict()
    for x in range(n):
        a[list(alphabet.keys())[x]] = list(alphabet.values())[x]
    return a

# main code starts here
if __name__ == "__main__":

    # start with an alphabet of only two characters
    alphabet_length = 2
    alpha = new_dictionary(alphabet_length)
    print(alpha)

    # sound the given letter(s)
    for x in alpha:
        sound_letter(x, alpha)
        Tone.sine(0, inter_char)
