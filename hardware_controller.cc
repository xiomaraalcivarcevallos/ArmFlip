/*
 * Project: ArmFlip - 7th Axis Gantry Control
 * Goal: Coordinate physical rotation with UR3e via Digital I/O Handshake
 */

#include <AccelStepper.h>

// Driver Pin Definition (e.g., A4988 or TB6600)
const int stepPin = 3;
const int dirPin = 4;
const int robotSignalPin = 7; // Input: Sync signal from UR3e
const int completionPin = 8;  // Output: Ready signal back to robot

// Stepper Motor Configuration
AccelStepper stepper(AccelStepper::DRIVER, stepPin, dirPin);

void setup() {
  pinMode(robotSignalPin, INPUT_PULLUP);
  pinMode(completionPin, OUTPUT);
  digitalWrite(completionPin, LOW);
  
  // Acceleration ramps for structural stability
  stepper.setMaxSpeed(1000);
  stepper.setAcceleration(500);
  
  // Serial communication for Gantry Data (Stream B)
  Serial.begin(9600); 
}

void loop() {
  // 1. Receive Target Position (Stream B)
  if (Serial.available() > 0) {
    long targetSteps = Serial.parseInt();
    stepper.moveTo(targetSteps);
  }

  // 2. Handshake Protocol (Synchronization)
  // Wait for the robot to signal it has reached its waypoint
  if (digitalRead(robotSignalPin) == HIGH) { 
    
    // Move the 7th-axis gantry to the calculated position
    while (stepper.distanceToGo() != 0) {
      stepper.run();
    }
    
    // 3. Confirm Step Completion
    digitalWrite(completionPin, HIGH); 
    delay(100); // Synchronization pulse
    digitalWrite(completionPin, LOW);
  }
}