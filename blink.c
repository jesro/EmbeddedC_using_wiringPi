#include <wiringPi.h>
int main(void){
wiringPiSetup();
pinMode(0,OUTPUT);  //GPIO pin 17
for(;;){
digitalWrite(0,HIGH);
delay(500);
digitalWrite(0,LOW);
delay(500);
}
return0;
}
