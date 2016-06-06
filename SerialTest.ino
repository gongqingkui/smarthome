/*
   SmartHome

  1602引脚图
  1602引脚 Arduino引脚 功能详解
  1        gnd            VSS一般接地
  2        +5v            VDD接电源（+5V）
  4        12            RS RS为寄存器选择，高电平1时选择数据寄存器、低电平0时选择指令寄存器。对应Arduino12
  6        11            EE(或EN)端为使能(enable)端，写操作时，下降沿使能。读操作时，E高电平有效
  11       5          DB4高4位三态、 双向数据总线 4位
  12       4            DB5高4位三态、 双向数据总线 5位
  13       3            DB6高4位三态、 双向数据总线 6位
  14       2            DB7高4位三态、 双向数据总线 7位（最高位）（也是busy flag）
  15                   BLA背光电源正极
  16                   BLK背光 电源负极
  DHT11引脚
  文字面是背面
  窗口面正面，左至右为+5v data GND
  数据引脚9
  Servo引脚 红+5v 棕GND 黄DATA
  数据引脚10
*/

#include <LiquidCrystal.h>
#include <dht11.h>
#include <Servo.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
dht11 DHT11;
Servo servo1;

#define DHT11PIN 9
String comdata = "";
float humidity = 0.0;
float temperature = 0.0;
char buffer[18];    //串口缓冲区的字符数组
void setup()
{
  Serial.begin(9600);
  Serial.flush();

  pinMode(13, OUTPUT);
  servo1.attach(10);
  Serial.println(DHT11LIB_VERSION);
  lcd.begin(16, 2);
  lcd.print("SmartHome");
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
  humidity = (float)DHT11.humidity;
  temperature = (float)DHT11.temperature;
  Serial.println(humidity, 2);
  Serial.println(temperature, 2);

  lcd.setCursor(10, 0);
  lcd.print(millis() / 1000);
  lcd.setCursor(0, 1);
  lcd.print(temperature);
  lcd.setCursor(10, 1);
  lcd.print(humidity);

  servo1.write(millis() / 1000);
  delay(2000);
}

void splitString(char *data)
{
  Serial.print("Data entered:");
  Serial.println(data);
  char *parameter;
  parameter = strtok(data, " ,");   //string token，将data按照空格或者,进行分割并截取
  Serial.print("***");
  Serial.println(parameter);
  while (parameter != NULL)
  {
    setLED(parameter);
    parameter = strtok(NULL, " ,");   //string token，再次分割并截取，直至截取后的字符为空
    Serial.print("---");
    Serial.println(parameter);
  }
  for (int x = 0; x < 16; x++)    //清空缓冲
  {
    buffer[x] = '\0';
  }
  Serial.flush();
}

void setLED(char *data)
{
  if ((data[0] == 'b') || (data[0] == 'B'))
  {
    int Ans = strtol(data + 1, NULL, 10); //10进制提取数据
    Ans = constrain(Ans, 0, 1);     //限制在0~255范围内
    if (Ans == 1) {
      digitalWrite(13, HIGH);
      delay(500);
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
