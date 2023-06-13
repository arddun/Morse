# MORSE CODE TRAINER SPECS



1. Send the first two letters, i.e. a b, few times to get the used to the sound.
2. Then send a set of those two letters, i.e. a b, randomly in blocks of five characters like a b a b b for five times.
3. Repeat the above without showing the letter.
4. Repeat the above but this time allowed key-stroke input. Display the input on screen then average the result. If less than 90% accuracy, start from point 1 again.
5. If 90%+ accuracy achieved, then add a letter, i.e. c, to the previous set, but still sending in blocks of five characters.
6. When reached the end of alphabet, start to add numbers to the sequence and repeat the process.
7. Able to adjust WPM speed.
8. Able to adjust pitch tone.
9. Able to receive input from morse-key and determine the character sent.




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


