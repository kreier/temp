// boot 
//
// submits successfull boot and wifi to
// http://temp.kreier.org/boot/boot.php
// results at
// https://kreier.org/temp/boot/
//
// Version 0.1.20121208
//

char version[14] = "0.1.20211208";

int ledPin = 2;
bool light = HIGH;    // LORA915, T-Koala, T8, Arduino
bool dark  = !light;
int count = 0; 

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
  Serial.println("Let's start!");
  Serial.print("This is version ");
  Serial.println(version);
  char ssid[23];
  uint64_t chipid = ESP.getEfuseMac(); // The chip ID is essentially its MAC address(length: 6 bytes).
  uint16_t chip = (uint16_t)(chipid >> 32); // copy highest 16 bit from chipid (48bit) to chip (16 bit)
  snprintf(ssid, 23, "MCUDEVICE-%04X%08X", chip, (uint32_t)chipid);
  Serial.print("The serial number is ");
  Serial.println(ssid);
  uint32_t chip2 = (uint32_t)(chipid);
  Serial.println(chip);
  Serial.println(chip, HEX);
  Serial.println(chip2);
  Serial.println(chip2, HEX);
  //Serial.print(chipid);
}

void loop() {
  digitalWrite(ledPin, light);
  Serial.print("LED on ");
  delay(50);
  digitalWrite(ledPin, dark);
  delay(100);
  digitalWrite(ledPin, light);
  delay(50);
  digitalWrite(ledPin, dark);
  Serial.print("LED off ");
  count++;
  if(count > 6) {
    count = 0;
    Serial.println(ledPin);
  }
  delay(10000);
}
