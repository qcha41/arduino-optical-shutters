#include <Servo.h>
String id = "ArduinoUnoRev3_55639303135351D0B172"; //do not change that
Servo servo;
int servoPorts[3] = {9,8,10};
char delimiter = ',';



void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}


void processCommand(String command){

  int equalPos = command.indexOf('=');

  if (equalPos != -1) {
    String servoName = command.substring(0,equalPos);

    int servoPort = 0;
    if (servoName == "SRV1") {
       servoPort = servoPorts[0];
    }
    else if (servoName == "SRV2") {
       servoPort = servoPorts[1];
    }
    else if (servoName == "SRV3") {
       servoPort = servoPorts[2];
    }

    if (servoPort != 0) {
       servo.attach(servoPort);
       int value = command.substring(equalPos+1,command.length()).toInt();
       servo.write(value);
       delay(400);
       servo.detach();       
    } 
  } 
}


void loop() {
  // put your main code here, to run repeatedly:
  
  if (Serial.available() > 0) {
    
    String input = Serial.readString();
    input.trim(); // To wash the string from whitespace, termination character..

    if (input == "ID?") {
      Serial.println(id);
    }
    else {
      
      int curs = 0;
      int delimPos = 0;
      while (delimPos != -1) {
        delimPos = input.indexOf(',', curs);
        String command = input.substring(curs,delimPos);
        processCommand(command);
        curs = delimPos+1;
      }

      Serial.println("done");

    }
  }
}






    
