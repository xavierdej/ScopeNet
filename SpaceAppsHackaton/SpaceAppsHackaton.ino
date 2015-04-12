#include <Servo.h>

#define LED 13


float azimuth = 90.0;
float elevation  = 45.0;

Servo servoAzimuth;
Servo servoElevation;

bool makeCapture = false; // Flag for serial commands
String inputString = "";

void setup()
{
	Serial.begin(9600);

	servoAzimuth.attach(9);
	servoElevation.attach(10);

	pinMode(LED, OUTPUT);
}

void loop()
{
	servoAzimuth.write(azimuth);
	servoElevation.write(elevation);
}


void serialEvent()
{
  while (Serial.available())
  {
    char inChar = (char)Serial.read();
    // inputString += inChar;
    if (inChar == 'a'|inChar == 'A')
    {
    	azimuth = Serial.parseFloat();
      Serial.print(azimuth);
    	digitalWrite(LED, HIGH);
		  delay(100);
		  digitalWrite(LED, LOW);
    }
    if (inChar == 'e'|inChar == 'E')
    {
      elevation = Serial.parseFloat();
      digitalWrite(LED, HIGH);
		delay(100);
		digitalWrite(LED, LOW);
    }
    if (inChar == 'c'|inChar == 'C')
    {
      makeCapture = true;
    }
  }
}