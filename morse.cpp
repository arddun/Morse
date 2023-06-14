//
// Program to convert an incoming ASCII string to the correct morse code dots and dashes
// and then use our on board LED to flash appropriately
//
// Author : alanm
//
// Date : Friday 27th November
//

#include <stdio.h>
#include <ctype.h>

#define LED        13
#define GAPINTRA  100  // gap between individual dots and dashes
#define GAPCHAR   200  // gap between ASCII characters (200 because we always terminate a char with a GAPINTRA
#define GAPWORD   600  // gap between words (600 not 700 for a similar reason)
#define DOT       100  // length of a dot
#define DASH      300  // length of a dash


// to hold the message that we send - maximum of 128 bytes
char message[128];

// 2D array which holds the morse code ranging from A-Z then 0-9
char morse[][6] = {{".--"},{"-..."},{"-.-."},{"-.."},{"."},{"..-."},
                   {"--."},{"...."},{".."},{".---"},{"-.-"},{".-.."},
                   {"--"},{"-."},{"---"},{".--."},{"--.-"},{".-."},
                   {"..."},{"-"},{"..-"},{"...-"},{".--"},{"-..-"},
                   {"-.--"},{"--.."},
                   {"-----"},{".----"},{"..---"},{"...--"},{"....-"},
                   {"....."},{"-...."},{"--..."},{"---.."},{"----."}
                 };

// sends a time delay of length ms
void sendGap (int length)
{
  digitalWrite (LED, LOW);
  delay (length);
} // void sendGap (int length)

// sends a dot or a dash depending on length
void sendMorseBit (int length)
{
  digitalWrite (LED, HIGH);
  delay (length);  
} // void sendMorseCharacter (int length)

// sends one morse character (i.e. an S or an A for example) - also sends all necessary gaps
void sendMorseCharacter (char *q)
{
  while (*q)
  {
    if (*q == '.')  sendMorseBit (DOT);
    else            sendMorseBit (DASH);
      
    sendGap (GAPINTRA);
    q++;
  }
  sendGap (GAPCHAR); 
} // void sendMorseCharacter (char *q)

// converts the message character by character into the appropriate morse strings of dots and dashes
void morseConversion ()
{
  char *p = message;
  char *q;
  int i;
  
  while (*p)                 // do this until there's nothing else to convert
  {  // check for 0 - 9
    if (*p >= '0' && *p <= '9')
    {
      i = *p;                // convert char to an integer
      q = morse [i-21];      // use the char code as an index into the morse array
      sendMorseCharacter (q);// passes a pointer to the correct morse string to the function
      Serial.println (q);    // send a message back to us showing what we're doing
    }
    else if (isalpha (*p))
    { // it's A-Z or a-z
      *p = toupper (*p);     // convert it to upper case
      i = *p;                // convert char to integer
      q = morse [i-65];      // use the char code as in index into the right place in the morse array
      sendMorseCharacter (q);// use the serial port to tell us what we're doing
      Serial.println (q);
    }
    else if (isspace (*p))   // it's a space between words so send a gap of the right length
      sendGap (GAPWORD);
  
    p++;                     // increment our pointer into the morse string
  }
  
} // void morseConversion ()


void convertMessage ()
{
  int incomingByte = 0;      // some initialisation
  int i = 0;
  message[0] = '\0';         // C strings are terminated by zero, so start with zero message length

  delay (50);                // need to wait to make sure we've got the whole string
  
  while (Serial.available() > 0) 
  {
    // read the incoming byte:
    incomingByte = Serial.read();
    message[i++] = incomingByte;  // add the byte to the message string
  }
  message[i] = '\0';              // terminate the string
  Serial.print ("Got ");          // tell us what we got
  Serial.println (message);
    
  morseConversion ();
} //void convertMessage ()


void setup ()
{
  pinMode (LED, OUTPUT);          // 13 is going to be our output pin
  Serial.begin (115200);          // our serial monitor will communicate at 115,200 baud
} // void setup ()


void loop ()
{
  int i;

  if (Serial.available () > 0)    // if there's a character on its way to us then
    convertMessage ();            // do something :)
} //void loop ()