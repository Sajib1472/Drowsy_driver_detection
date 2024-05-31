#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ArduinoJson.h>
#include <LiquidCrystal.h>

#define BUZZER_PIN D1 


const char* ssid = "Hello";
const char* password = "sajib1471";

ESP8266WebServer server(80);



void setup() {
  Serial.begin(115200);
  delay(10);

  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  server.on("/test", HTTP_POST, handlePost); 
  server.begin();
  Serial.println("HTTP server started");


  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(2, OUTPUT); 
}

void loop() {
  server.handleClient();
}

void handlePost() {
  String receivedData = server.arg("plain");

  DynamicJsonDocument doc(1024);
  deserializeJson(doc, receivedData);

  const char* state = doc["state"];

  Serial.print("Received state: ");
  Serial.println(state);

  if (strcmp(state, "sleeping") == 0 || strcmp(state, "drowsy") == 0) {
    digitalWrite(BUZZER_PIN, HIGH);
    digitalWrite(2, HIGH); 
    
    

    Serial.println("Wake up! Danger!");

  } else {
    digitalWrite(BUZZER_PIN, LOW);
    digitalWrite(2, LOW); 
    

    Serial.println("ESP8266 Ready");
  }

  server.send(200, "text/plain", "OK"); 
}
