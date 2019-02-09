#include <Servo.h>

#define LeftSenter 10
#define RightSenter 160
#define HandEnd 125

Servo Hand;
Servo Left;
Servo Right;
String State; //move, stuck, grab, need help
int functions[2];

void setup() {
  functions = (
    "capture",
    "release"
  )
  
  delay(1000);
  Serial.begin(9600);
  Serial.println("BEGIN");
  Serial.println("Print 'Help' for all commands");
  
  Hand.attach(3);
  Left.attach(4);
  Right.attach(5);
  pinMode(6, INPUT);
  
  Left.write(LeftSenter);
  Right.write(RightSenter);
  Hand.write(HandEnd);
}

void loop() {
  String str = Serial.readString();

  if (str != "") {
    Serial.println(str);
  }
  if (str == "help") {
    for() {
      Serial.println();
    }
    //Serial.println("  capture");
    //Serial.println("  release");
  }
  if (str == "capture") {
    Hand.write(10);
  }
  if (str == "release") {
    Hand.write(HandEnd);
  }
}
