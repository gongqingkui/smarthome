/*
  SmartHome
  1602引脚 Arduino引脚 功能详解
  1        gnd          VSS一般接地
  2        +5v          VDD接电源（+5V）
  4        13           RS RS为寄存器选择，高电平1时选择数据寄存器、低电平0时选择指令寄存器。对应Arduino12
  6        12           EE(或EN)端为使能(enable)端，写操作时，下降沿使能。读操作时，E高电平有效
  11       5            DB4高4位三态、 双向数据总线 4位
  12       4            DB5高4位三态、 双向数据总线 5位
  13       3            DB6高4位三态、 双向数据总线 6位
  14       2            DB7高4位三态、 双向数据总线 7位（最高位）（也是busy flag）
  DHT11引脚 窗口面正面，左至右为 +5v data GND
  Servo引脚 红+ 5v   棕GND   黄DATA
  甲醛传感器 VCC RXD TXD GND 接串口
*/
#include <LiquidCrystal.h>
#include <dht11.h>
#include <Servo.h>
#include <SoftwareSerial.h>

#define DHT11PIN 6
#define servo1Pin 7
#define servo2Pin 8

LiquidCrystal lcd(13, 12, 5, 4, 3, 2);
dht11 DHT11;
Servo servo1;
Servo servo2;
SoftwareSerial mySerial(9, 10);
char buffer[18];    //串口缓冲区的字符数组

void setup()
{
  servo1.attach(servo1Pin);
  servo2.attach(servo2Pin);

  Serial.begin(9600);
  Serial.flush();
  Serial.println(DHT11LIB_VERSION);

  Serial.println("JQbegin");
  mySerial.begin(9600);

  pinMode(13, OUTPUT);
  lcd.begin(16, 2);
  lcd.setCursor(10, 0);
  lcd.print("C:");
  lcd.setCursor(0, 1);
  lcd.print("T:");
  lcd.setCursor(10, 1);
  lcd.print("H:");
}

void loop()
{
  if (Serial.available() > 0)     //Serial.available()返回串口收到的字节数
  {
    int index = 0;
    delay(100);             //延时等待串口收完数据，否则刚收到1个字节时就会执行后续程序
    int numChar = Serial.available();
    if (numChar > 15)         //确认数据不会溢出，应当小于缓冲大小
    {
      numChar = 15;
    }
    while (numChar--)
    {
      buffer[index++] = Serial.read();  //将串口数据一字一字的存入缓冲
    }
    splitString(buffer);        //字符串分割
  }

  String jqStr = "0.0000";
  String Temp = "0.0000";
  String Humi = "0.0000";
  //JQ
  jqStr = readJQ();
  delay(1000);
  Serial.println("C:" + jqStr);
  //Temp
  Temp = readTemp();
  delay(1000);
  Serial.println("T:" + Temp);
  //Humi
  Humi = readHumi();
  delay(1000);
  Serial.println("H:" + Humi);

  lcd.setCursor(12, 0);
  lcd.print(jqStr);
  lcd.setCursor(2, 1);
  lcd.print(Temp);
  lcd.setCursor(12, 1);
  lcd.print(Humi);

  servo1.write((millis() / 1000) % 180);
  servo2.write(180 - ((millis() / 1000) % 180));
  delay(1000 * 30);
}
float readTemp() {
  int chk = DHT11.read(DHT11PIN);
  switch (chk)
  {
    case DHTLIB_OK:
      Serial.println("OK");
      break;
    case DHTLIB_ERROR_CHECKSUM:
      Serial.println("Checksum error");
      break;
    case DHTLIB_ERROR_TIMEOUT:
      Serial.println("Time out error");
      break;
    default:
      Serial.println("Unknown error");
      break;
  }
  return (float)DHT11.temperature;
}
float readHumi() {
  int chk = DHT11.read(DHT11PIN);
  switch (chk)
  {
    case DHTLIB_OK:
      Serial.println("OK");
      break;
    case DHTLIB_ERROR_CHECKSUM:
      Serial.println("Checksum error");
      break;
    case DHTLIB_ERROR_TIMEOUT:
      Serial.println("Time out error");
      break;
    default:
      Serial.println("Unknown error");
      break;
  }
  return  (float)DHT11.humidity;
}
void splitString(char *data)
{
  Serial.print("Data entered:");
  Serial.println(data);
  char *parameter;
  parameter = strtok(data, " ,");   //string token，将data按照空格或者,进行分割并截取 只要最前一个字串
  while (parameter != NULL)
  {
    setLED(parameter);
    parameter = strtok(NULL, " ,");   //string token，再次分割并截取，直至截取后的字符为空,数据抛弃，不用管
    Serial.print("---");
    Serial.println(parameter);
  }
  for (int x = 0; x < 16; x++)    //清空缓冲
  {
    buffer[x] = '\0';
  }
  Serial.flush();
}

/*
   根据首字母b d s 来给具体安排反应
   b 0 1 闪LED灯
   d 数字 设servo角度
   s string 用液晶显示
*/
void setLED(char *data)
{
  if ((data[0] == 'b') || (data[0] == 'B'))
  {
    int Ans = strtol(data + 1, NULL, 10); //10进制提取数据
    Ans = constrain(Ans, 0, 1);     //限制在0~255范围内
    if (Ans == 1) {
      digitalWrite(13, HIGH);
      delay(2500);
      digitalWrite(13, LOW);
    }
    Serial.print("binary is set to :");
    Serial.println(Ans);
  }
  if ((data[0] == 'd') || (data[0] == 'D'))
  {
    int Ans = strtol(data + 1, NULL, 10);
    Ans = constrain(Ans, 0, 180);
    servo1.write(Ans);
    delay(1000);
    Serial.print("ditital is set to :");
    Serial.println(Ans);
  }
  if ((data[0] == 's') || (data[0] == 'S'))
  {
    Serial.print("String is set to :");
    lcd.setCursor(0, 0);
    lcd.print(data + 1);
    Serial.println(data + 1);
  }
}
float readJQ() {
  unsigned char hexdata[5] = {0xA5, 0x5A, 0x02, 0x80, 0xAA};
  unsigned char cnt = 0;
  unsigned char c ;
  long hchodata = 99999999L;
  float hcho = 0.8888;
  mySerial.write(hexdata, 5);
  delay(200);
  while (mySerial.available()) {
    c = mySerial.read();
    delay(1);
    //Serial.print(c, HEX); Serial.print(' ');
    cnt++;
    if (cnt == 5) {//第五位*156
      hchodata = c * 256;
    }
    if (cnt == 6) {
      hchodata += c;
    }
    if (c == 170) {//最后一位
      hcho = ((float)hchodata / 100);
      return hcho;
    }
  }
}
