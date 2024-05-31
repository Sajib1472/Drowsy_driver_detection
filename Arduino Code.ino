#include <Arduino.h>

const int signalPin = 2;  

const int enA = 9;  
const int in1A = 8; 
const int in2A = 7;  

const int enB = 6;   
const int in1B = 12;  
const int in2B = 11;  
 
int motorSpeedA = 0; 
int motorSpeedB = 0; 

void setup() {
  
  pinMode(signalPin, INPUT); 

  pinMode(enA, OUTPUT);
  pinMode(in1A, OUTPUT);
  pinMode(in2A, OUTPUT);

  pinMode(enB, OUTPUT);
  pinMode(in1B, OUTPUT);
  pinMode(in2B, OUTPUT);

  analogWrite(enA, 0);
  digitalWrite(in1A, LOW);
  digitalWrite(in2A, LOW);

  analogWrite(enB, 0);
  digitalWrite(in1B, LOW);
  digitalWrite(in2B, LOW);
}

void loop() {
  int signal = digitalRead(signalPin);  

  if (signal == HIGH) {
    motorSpeedA = 128;
    motorSpeedB = 128; 

    analogWrite(enA, motorSpeedA);
    digitalWrite(in1A, HIGH);
    digitalWrite(in2A, LOW);

    analogWrite(enB, motorSpeedB);
    digitalWrite(in1B, HIGH);
    digitalWrite(in2B, LOW);

    delay(2000);
    
    analogWrite(enA, 0);
    digitalWrite(in1A, LOW);
    digitalWrite(in2A, LOW);

    analogWrite(enB, 0);
    digitalWrite(in1B, LOW);
    digitalWrite(in2B, LOW);
    delay(10000);
  } else {
    
    analogWrite(enA, 255);
    digitalWrite(in1A, HIGH);
    digitalWrite(in2A, LOW);

    analogWrite(enB, 255);
    digitalWrite(in1B, HIGH);
    digitalWrite(in2B, LOW);
  }
}