#include <NTPClient.h>
#include <WiFiUdp.h>
#include <splash.h>
#include <ESP8266WiFi.h>
#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Wire.h>

#define buzzer D7
#define SCREEN_WIDTH 128 
#define SCREEN_HEIGHT 32 
#define STASSID "SSID"            //Need Change!!
#define STAPSK  "Password"        //Need Change!!
#define GMT8 28800 // Hong Kong

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);


const char* ssid = STASSID;
const char* password = STAPSK;
char daysOfTheWeek[7][12] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
int val = 0 ;

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP,"stdtime.gov.hk",GMT8);                //Hong Kong observatory
WiFiServer server(80);
WiFiClient client;

void setup() {
  int wificheck = 0;
    Serial.begin(115200);
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {              
    Serial.println(F("SSD1306 allocation failed"));
    for(;;);
  }
  displayopening();
  pinMode(buzzer, OUTPUT);
  digitalWrite(buzzer, 0);
  Serial.println();
  Serial.println();
  Serial.print(F("Connecting to "));
  Serial.println(ssid);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(F("."));
    wificheck ++;
      if(wificheck >20){                    //10 Sec
      displayfailconnect();
    }
  }

  Serial.println();
  Serial.println(F("WiFi connected"));
  server.begin();
  Serial.println(F("Server started"));
  Serial.println(WiFi.localIP());
  timeClient.begin();

}

void loop() {
  client = server.available();
   displayip(val);
  if (!client) {
    return;
  }
  client.setTimeout(5000); 
  String req = client.readStringUntil('\r');
  if (req.indexOf(F("/Buzzer/0")) != -1) {
    val = 0;
  } else if (req.indexOf(F("/Buzzer/1")) != -1) {
    val = 1;
  } else {
    Serial.println(F("invalid request"));
    val = digitalRead(buzzer);
  }
  while (client.available()) {
    client.read();
  }
    digitalWrite(buzzer, val);
  client.print(F("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<!DOCTYPE HTML>\r\n<html>\r\nStatus now "));
  client.print((val) ? F("high") : F("low"));
  client.print(F("<br><br>Click <a href='http://"));
  client.print(WiFi.localIP());
  client.print(F("/Buzzer/1'>here</a> to turn on, or <a href='http://"));
  client.print(WiFi.localIP());
  client.print(F("/Buzzer/0'>here</a> to turn off.</html>"));
}

void displayfailconnect(){
   display.clearDisplay();
  delay(1000);
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0, 0);
  display.println("Fail to connect WIFI");
  display.println("Plz check your SSID");
  display.println("Plz check your password");
  display.display();
}



void displayopening(){
  display.clearDisplay();
  delay(1000);
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0, 0);
  display.print("Connecting to WIFI");
  display.display(); 
}

void displayip(int onoff){
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0, 0);
  timeClient.update();
  display.print(daysOfTheWeek[timeClient.getDay()]);
  display.print(", ");
  display.println(timeClient.getFormattedTime());
  display.print("SSID:");
  display.println(ssid);
  display.print("IP:");
  display.println(WiFi.localIP());
  digitalWrite(buzzer, onoff);
  if(onoff == 0){
      display.print("Status: OFF   ");
      display.print(buzzer);
      display.display(); 
   }else{
      display.print("Status: ON    ");
      display.print(buzzer);
      display.display(); 
  }
  delay(1);
}
