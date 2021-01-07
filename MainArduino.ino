#include <SoftwareSerial.h>
#include "TFMini.h"

#include <Wire.h>

SoftwareSerial mySerial(10, 11);      // Uno RX (TFMINI TX), Uno TX (TFMINI RX)
TFMini tfmini;
int x;

int c=999;
int b=1;
int a = 0;

void setup() {
  
  Serial.begin(115200); 
  Wire.begin(9);
  Wire.onReceive(receiveEvent);
  mySerial.begin(TFMINI_BAUDRATE);
  tfmini.begin(&mySerial);  


  
}
void receiveEvent()
{
  x = Wire.read();
}
void loop() {

  uint16_t dist = tfmini.getDistance();
 
  
  
  
  Serial.print(dist);
  Serial.print(" ");
  Serial.println(x);

  
 
}
