# MORSE CODE TRAINER SPECS



1. Begin with an alphabet of two letters, 'a'  and 'b'. Sound the letter 'a' ten times with a one second silent pause between letters. Pause for one second then sound the letter 'b' ten times with a one second silent pause between letters. 
2. Choose a five letter random selection of letters from the alphabet. Display the sequence while sounding the letters sequentially with a one second pause between letters. Repeat five times each time with a different random sequence. 
3. Repeat 2 but after each sequence is sounded wait for the user to enter their guess as to which sequence they had just heard. Display the correct sequence on screen. Compare the correct sequence with the user's guess. If, after five sequences have been heard and evaluated, the user had more than 1 sequence incorrect, repeat this step.
4. Otherwise add the next letter in the English alphanumeric alphabet to our alphabet (numbers follow letters). Sound the new character ten times with a one second pause between letters to accustom the user to the sound. Return to step 2.
5. The user should be able to adjust the word per minute (WPM) speed.
6. The user should be allowed to chose the frequency of the tone that they hear. The default will be A=440.
7. In later iterations the user will receive input from a simulated morse-key to determine the character sent.
8. In later iterations the user will be sent real world text sequences chosen from random publications.




## General rules in Morse code.

- The length of a dot is 1 time unit
- A dash is 3 time units
- The space between symbols (dot & dashes) of the same letter is 1 time unit.
- The space between letters is 3 time units
- The space between words is 7 time unit.

| Character | Code |
| --- | --- |
|A| . - |
|B| - . . .|
|C| - . - .|
|D| - . .|
|E| . |
|F| . . - .|
|G| - - .|
|H| . . . .|
|I| . . |
|J| . - - - |
|K| - . -|
|L| . - . .|
|M| - -|
|N| - .|
|O| - - -|
|P| . - - .|
|Q| - - . -|
|R| . - .|
|S| . . .|
|T| -|
|U| . . -|
|V| . . . -|
|W| . - -|
|X| - . . -|
|Y| - . - -|
|Z| - - . .|
|1| . - - - -|
|2| . . - - -|
|3| . . . - -|
|4| . . . . -|
|5| . . . . .|
|6| - . . . . |
|7| - - . . .|
|8| - - - . .|
|9| - - - - .|
|0| - - - - -|

## Calculating Morse Code Speed
- The word PARIS is the standard for determing CW code speed. Each dit is one element, each dah is three element, intra-character spacing is one element, inter-character spacing is three elements and inter-word spacing is seven elements. The word PARIS is exactly 50 elements.

- Note that after each dit/dah of the letter P -- one element spacing is used except the last one (intra-character).

- After the last dit of P is sent, 3 elements are added (inter-character).
- After the word PARIS - 7 elements are used.

Thus:  
P = di da da di = 1 1 3 1 3 1 1 (3) = 14 elements.  
A = di da = 1 1 3 (3) = 8 elements.  
R = di da di = 1 1 3 1 1 (3) = 10 elements.  
I = di di = 1 1 1 (3) = 6 elemets.  
S = di di di = 1 1 1 1 1 [7] = 12 elements.  

Total = 50 Elements.  
() = inter-character.  
[] = inter-word.  

If you send PARIS 5 times in a minute (5WPM) you have sent 250 elements (using correct spacing). 250 elements into 60 second per minute = 240 milliseconds per element.

13 WPM is one element every 92.31 milliseconds.

The Farnsworth method sends the dits and dahs and intra-character spacing at a higher speed, then increasing the inter-character and the inter-word spacing to slow the sending speed down to the overall speed. For example, to send at 5 WPM with 13 WPM character in Farnsworth method, the dits and intra-character spacing would be 92.3 milliseconds, the dah would be 276.9 milliseconds, the inter-character spacing would be a 3.367 seconds.


