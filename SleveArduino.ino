#include <Servo.h> 
#include <Wire.h>

int servoPin = 3; 
int servoPin2 = 2;
int check = 0;
int a,d = 0;
int b = 1;
int c = 999;
int dist = 0;


Servo Servo11; 


void setup() { 
   
   Servo11.attach(servoPin);
   Wire.begin(9);
   Serial.begin(115200); 
   
   
}

void loop(){ 
  while(c >= 997)
  {
   Servo11.write(0); 
   a=a+3;
   b=b+1;
   
   if(b >= 180)
   {
    b=179;
   }
   if(a >= 997)
   {
    d=1;
    c=0;
   }
   Wire.beginTransmission(9); 
   Wire.write(b);              
   Wire.endTransmission();
   Serial.println(b);
   delay(3); 
  }

 

  
   while(a >= 997)
   {
   if(d>0)
   { 
   Servo11.write(180); 

   d=0;
   b=b-1;
   c=c+3;
   
   if(b < 1)
   {
    b=1;
   }
   if(c >= 997)
   {
    a=0;
    
   }
   Wire.beginTransmission(9); 
   Wire.write(b);              
   Wire.endTransmission();
   Serial.println(b);
   delay(3);
   }
}
}
