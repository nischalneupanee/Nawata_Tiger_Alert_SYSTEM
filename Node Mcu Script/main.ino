#include <ESP8266WiFi.h>
#include <ESP8266mDNS.h>
#include <ESP8266WebServer.h>

const char* ssid = "YourSSID";          // Replace with your WiFi SSID
const char* password = "YourPassword";  // Replace with your WiFi Password

ESP8266WebServer server(80);  // Create a web server on port 80

const int ledPin = 14;  // D5 pin is GPIO14

void handleAlert() {
  Serial.println("Alert received");  // Log when alert is received
  digitalWrite(ledPin, HIGH);  // Turn on LED (HIGH turns the LED on)
  delay(3000);                // Wait for 3 seconds
  digitalWrite(ledPin, LOW);  // Turn off LED
  server.send(200, "text/plain", "LED lit for 3 seconds");
}

void setup() {
  // Start Serial for debugging
  Serial.begin(115200);
  Serial.println();

  // Setup LED pin as output
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);  // Make sure LED is off initially

  // Connect to WiFi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");

  // Start the mDNS responder
  if (MDNS.begin("esp8266")) {
    Serial.println("mDNS responder started");
  } else {
    Serial.println("Error setting up mDNS responder");
  }

  // Define a route that will trigger the LED
  server.on("/alert", handleAlert);

  // Start the web server
  server.begin();
  Serial.println("HTTP server started");

  // Print the IP address
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  // Handle any incoming HTTP requests
  server.handleClient();

  // You need to call MDNS.update() regularly
  MDNS.update();
}
