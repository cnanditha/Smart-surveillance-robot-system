# Smart-surveillance-system
The Smart Surveillance Robot is an AI-powered IoT monitoring system built with ESP32-CAM, L298N, and YOLOv8. It streams live video over Wi-Fi, supports browser-based remote navigation, and performs real-time object detection through host-side processing.
#ESP32-CAM Spy Robo Car
This repository contains the code and instructions for building a remote-controlled surveillance car using an ESP32-CAM module and an L298N motor driver. The project allows you to control the car and stream a live video feed directly from a smartphone web browser over a local WiFi network.
#Project Images
Hardware Setup: See the file named Robot image.jpeg for the fully assembled car.
Web Interface: See the file named Robot demo.jpeg for the smartphone control dashboard, showing the video feed and movement buttons.
#Hardware Requirements
ESP32-CAM Module
L298N Motor Driver Shield
FTDI Programmer Module (needed to upload code)
2-Wheel or 4-Wheel Car Chassis Kit with DC motors
2x 3.7V 18650 Lithium Cells (1200mAh+) 
Compatible battery holderPower Switch and Jumper Wires
#Setup and Installation
1. Programming the ESP32-CAM
Connect the ESP32-CAM to your computer using the FTDI programmer.
Open the main sketch file in the Arduino IDE.
Update the WiFi credentials in the code.
Select your board in the Arduino IDE (ESP32 Wrover Module).
Upload the sketch.
2. Getting the IP Address
Remove the jumper wire between GPIO 0 and GND.
Open the Arduino Serial Monitor and set the baud rate to 115200.
Press the reset button on the ESP32-CAM.
Wait for the module to connect to your WiFi network. The Serial Monitor will print the local IP address
3. Assembly and Running
Assemble the hardware components on the car chassis according to the pin connections.
Turn on the power switch.
Connect your smartphone to the same WiFi network as the ESP32-CAM.
Open a web browser and navigate to the IP address from the previous step.
#Repository Structure
ESP32_Cam_Car.ino: The main Arduino sketch that initializes the camera, connects to WiFi, and sets up the web servers.
app_httpd.cpp: Contains the web server logic, HTTP handlers for the video stream, and movement endpoints (/go, /back, /left, /right, /stop, /ledon, /ledoff).
camera_index.h: A compressed byte array containing the HTML interface.
#Video reference:
https://youtu.be/C-EoBkRQ1M0?si=ciys91pVzXv9lRM0
