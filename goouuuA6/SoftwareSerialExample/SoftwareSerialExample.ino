#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX
int i = 1;
void setup() {
  Serial.begin(115200);
  while (!Serial) {
    ;
  }
  Serial.println("Hardware Serial Working");
  mySerial.begin(115200);
  while (!mySerial) {
    ;
  }
  Serial.println("Software Serial Working");
  //mySerial.println("ATD15133760632;");
}

void loop() {
  if (mySerial.available()) {
    Serial.print((char)mySerial.read());
    delay(1);
  }
  if (Serial.available()) {
    mySerial.print((char)Serial.read());
    delay(1);
  }
  if (i == 1) {
    sendTcp("a"); 
    i = i - 1;
  }
}
int sendTcp(String var) {
  mySerial.println("AT+CGATT=1");
  //delay(2000);
  mySerial.println("AT+CGACT=1,1");
  //delay(3000);
  mySerial.println("AT+CIFSR");
  //delay(500);
  mySerial.println("AT+CIPCLOSE");
  //delay(3000);
  mySerial.println("AT+CIPSTART=TCP,gongqingkui.vicp.cc,15048");
  //delay(5000);
  mySerial.println("AT+CIPSTATUS");
  //delay(500);
  mySerial.println("AT+CIPSEND");
  //delay(500);
  mySerial.print(var);
  mySerial.println(0x1A);
  //delay(2000);
  mySerial.println("AT+CIPCLOSE");
}
