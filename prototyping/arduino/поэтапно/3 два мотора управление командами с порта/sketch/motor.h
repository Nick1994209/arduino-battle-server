#include "Arduino.h"

// зарезервированы буквы: w, s, a, d, b
class Motor
{
  public:
    Motor(int _EN1, int _IN1, int _IN2, int _EN2, int _IN3, int _IN4); 
    ~Motor();  
    
    int EN1, IN1, IN2, EN2, IN3, IN4;
    char cur_data_port;
    char last_data_port = 'govno';
    int i;

    void MotorBrake();
    void MotorGo();
    void MotorGoesBack();
    void MotorGoesRight();
    void MotorGoesLeft();
    
    void SwitchMove(char usb_port_data);
};

Motor::Motor(int _EN1, int _IN1, int _IN2, int _EN2, int _IN3, int _IN4)
{
  EN1 = _EN1; // EN1 - напряжение для первого мотора (ENA)
  IN1 = _IN1; // первый мотор
  IN2 = _IN2; // первый мотор
  EN2 = _EN2; // ENB
  IN3 = _IN3;
  IN4 = _IN4;
  
  pinMode(EN1, OUTPUT);
  pinMode(EN2, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
}
Motor::~Motor(){}

void Motor::MotorBrake ()
{
  analogWrite(EN1, 0);
  analogWrite(EN2, 0);
  digitalWrite (IN2, LOW);
  digitalWrite (IN1, LOW); 
  digitalWrite (IN4, LOW);
  digitalWrite (IN3, LOW); 
  delay(500);
}

void Motor::MotorGo ()
{ 
  MotorBrake(); //пока так
  
  digitalWrite (IN2, HIGH);
  digitalWrite (IN1, LOW); 
  digitalWrite (IN4, HIGH);
  digitalWrite (IN3, LOW); 
  for (i = 0; i < 180; i++)
  {
      analogWrite(EN1, i);
      analogWrite(EN2, i);
      delay(10);
  }
}

void Motor::MotorGoesBack ()
{ 
  MotorBrake();
  
  digitalWrite (IN2, LOW);
  digitalWrite (IN1, HIGH); 
  digitalWrite (IN4, LOW);
  digitalWrite (IN3, HIGH); 
  for (i = 0; i <= 180; i++)
  {
      analogWrite(EN1, i);
      analogWrite(EN2, i);
      delay(10);
  }
}

void Motor::MotorGoesRight()
{
  MotorBrake();

  // проверить! 
  //крутит левое вперед, правое - назад
  digitalWrite (IN2, HIGH);
  digitalWrite (IN1, LOW); 
  
  digitalWrite (IN4, LOW);
  digitalWrite (IN3, HIGH);
  for (i = 0; i <= 180; i++)
  {
    analogWrite(EN1, i);
    analogWrite(EN2, i);
    delay(10);
  }
}

void Motor::MotorGoesLeft()
{
  MotorBrake();

  // проверить! 
  //крутит левое вперед, правое - назад
 
  digitalWrite (IN2, LOW);
  digitalWrite (IN1, HIGH); 
  
  digitalWrite (IN4, HIGH);
  digitalWrite (IN3, LOW);  
  for (i = 0; i <= 180; i++)
  {
      analogWrite(EN1, i);
      analogWrite(EN2, i);
      delay(10);
  }
}

void Motor::SwitchMove(char usb_port_data)
{
  cur_data_port = usb_port_data;
  
  if (last_data_port != cur_data_port ) 
    { 
      char last_data_port = cur_data_port;
      switch (cur_data_port) //читаем переменную (по 1 символу) с порта
      { 
        case 'w':
        {
          Serial.println(cur_data_port);
          MotorGo();
           break;
        }
      
        case 's':
        {
          Serial.println(cur_data_port);
          MotorGoesBack();
           break;
        }
      
        case 'b':
        { 
          Serial.println(cur_data_port);
          MotorBrake();
           break;
        }
          
        case 'd':
        { 
          Serial.println(cur_data_port);
          MotorGoesRight();
           break;
        }
        case 'a':
        { 
          Serial.println(cur_data_port);
          MotorGoesLeft();
           break;
        }
      } 
    }
}
