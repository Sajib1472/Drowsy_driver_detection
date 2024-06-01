# Driver Drowsiness Detection System

## Overview
This project aims to enhance road safety by developing a Driver Drowsiness Detection System using an ESP32 webcam for image processing. The system identifies the sleep or drowsy state of the driver in real-time and communicates this state to an ESP8266 module. The ESP8266 then sends signals to an Arduino to control the vehicle's operation, slowing down or stopping the car when the driver is detected to be drowsy, and allowing normal operation when the driver is alert.

## Objectives
1. **Real-Time Drowsiness Detection**: Utilize an ESP32 webcam to capture and process images of the driver to detect signs of drowsiness in real-time.
2. **Image Processing Implementation**: Implement image processing techniques on the ESP32 to accurately identify drowsy states through indicators such as prolonged eye closure, yawning, or head nodding.
3. **Data Communication**: Use JSON files to transmit the driver's state from the ESP32 to the ESP8266 reliably.
4. **Microcontroller Integration**: Integrate the ESP32, ESP8266, and Arduino to facilitate accurate and timely responses to the detected drowsy state.
5. **Automated Vehicle Control**: Program the ESP8266 to send signals to the Arduino to control the vehicle’s speed based on the driver's state—slowing down or stopping the vehicle when drowsiness is detected and allowing normal operation when the driver is alert.
6. **Safety Enhancement**: Reduce the risk of accidents caused by driver drowsiness through automated intervention.
7. **System Reliability**: Ensure the system operates reliably under various conditions, providing consistent and accurate drowsiness detection and response.
8. **Low Power Consumption**: Optimize the system for low power consumption for long-term use in vehicles.
9. **Scalability and Adaptability**: Design the system to be easily scalable and adaptable for integration into different vehicles and driving environments.
10. **User-Friendly Interface**: Provide an easy-to-use interface for setting up and monitoring the system.

## Introduction
Driver drowsiness is a significant factor contributing to road accidents worldwide. Fatigue impairs driving ability, reaction time, and decision-making, posing a serious threat to road safety. To mitigate this risk, technological solutions can be employed to monitor the driver's state and take preventive actions when drowsiness is detected.

This project leverages the capabilities of the ESP32 and ESP8266 microcontrollers along with an Arduino to create a comprehensive driver drowsiness detection system. The ESP32, equipped with a webcam, captures real-time images of the driver and processes these images to detect signs of drowsiness. Once drowsiness is detected, the ESP32 sends this information in the form of a JSON file to the ESP8266 module. The ESP8266 then communicates with an Arduino to control the vehicle's operation, ensuring a timely response to prevent accidents.

## System Components
- **ESP32 with Webcam**: Captures and processes images of the driver to detect signs of drowsiness.
- **ESP8266 Module**: Receives the driver's state from the ESP32 and sends signals to the Arduino.
- **Arduino**: Controls the vehicle’s speed based on the signals received from the ESP8266.

## Workflow
1. **Image Capture**: The ESP32 webcam captures real-time images of the driver.
2. **Image Processing**: The ESP32 processes the images to detect drowsiness using indicators such as prolonged eye closure, yawning, or head nodding.
3. **Data Transmission**: The ESP32 sends the detected state in a JSON file to the ESP8266.
4. **Signal Communication**: The ESP8266 sends high or low signals to the Arduino based on the driver's state.
5. **Vehicle Control**: The Arduino adjusts the vehicle’s speed accordingly—slowing down or stopping the vehicle when drowsiness is detected and allowing normal operation when the driver is alert.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Sajib1472/Drowsy_driver_detection.git
   ```
2. **Upload Code**:
   - Upload the ESP32 code to your ESP32 module.
   - Upload the ESP8266 code to your ESP8266 module.
   - Upload the Arduino code to your Arduino board.
3. **Connect Hardware**:
   - Connect the ESP32, ESP8266, and Arduino according to the provided schematic.

## Schematic Diagram:
              +----------------+
           |    ESP8266     |
           |                |
           |   D1 (BUZZER)  |------> Buzzer
           |                |
           |   GPIO2        |------> Arduino Uno Pin 2
           +----------------+
                     |
                     |
                     v
           +----------------+
           |   Arduino Uno  |
           |                |
           |  D2 <----------|---+
           |                |   |
           |  D9 (ENA)      |---|--> L293D Pin 1 (ENA)
           |  D8 (IN1)      |---|--> L293D Pin 2 (IN1)
           |  D7 (IN2)      |---|--> L293D Pin 7 (IN2)
           |  D6 (ENB)      |---|--> L293D Pin 9 (ENB)
           |  D12 (IN3)     |---|--> L293D Pin 10 (IN3)
           |  D11 (IN4)     |---|--> L293D Pin 15 (IN4)
           |                |
           |  GND           |---|--> L293D Pins 4, 5, 12, 13 (GND)
           |  5V            |---|--> L293D Pins 8, 16 (VCC)
           +----------------+
                     |
                     |
                     v
           +----------------+
           |    L293D IC    |
           |                |
           | Motor A        |
           |  Pin 3 (OUT1)  |---|--> Motor A Terminal 1
           |  Pin 6 (OUT2)  |---|--> Motor A Terminal 2
           |                |
           | Motor B        |
           |  Pin 11 (OUT3) |---|--> Motor B Terminal 1
           |  Pin 14 (OUT4) |---|--> Motor B Terminal 2
           +----------------+
           
## Detailed Steps:
1. **Connect the ESP8266 to the Arduino Uno:**
   - Connect ESP8266 GPIO2 to Arduino digital pin 2.
   - Connect ESP8266 D1 to the positive leg of the buzzer and the negative leg to GND.

2. **Connect the Arduino Uno to the L293D Motor Driver:**
   - Arduino digital pin 9 to L293D ENA (Pin 1).
   - Arduino digital pin 8 to L293D IN1 (Pin 2).
   - Arduino digital pin 7 to L293D IN2 (Pin 7).
   - Arduino digital pin 6 to L293D ENB (Pin 9).
   - Arduino digital pin 12 to L293D IN3 (Pin 10).
   - Arduino digital pin 11 to L293D IN4 (Pin 15).
   - Arduino GND to L293D GND pins (4, 5, 12, 13).
   - Arduino 5V to L293D VCC pins (8, 16).

3. **Connect the DC Motors to the L293D Motor Driver:**
   - Connect Motor A to L293D output pins 3 and 6.
   - Connect Motor B to L293D output pins 11 and 14.

## Power Supply:
1. Ensure that the Arduino Uno is powered via USB or an external power supply.
2. Ensure the L293D is properly powered with 5V and GND connections.

## Usage
1. Power on the system.
2. The ESP32 will start capturing and processing images of the driver.
3. If drowsiness is detected, the ESP8266 will send a high signal to the Arduino, causing the vehicle to slow down or stop.
4. If the driver is alert, a low signal will be sent, allowing the vehicle to operate normally.

## Contributing
We welcome contributions to enhance the system's functionality, reliability, and performance. Please fork the repository and submit pull requests with your improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This project demonstrates the practical application of IoT (Internet of Things) and image processing to improve road safety measures by preventing accidents caused by driver drowsiness.
