#include "motor.h"

// мотор
const int EN1 = 3; // упр 1-ым enA правое
const int IN1 = 2; // контролер 1 для левого мотора - (певый)
const int IN2 = 5; // контролер 2 для левого мотора

const int EN2 = 6; // упр 1-ым мотором  enB левое
const int IN3 = 7; // управление вторым мотором
const int IN4 = 8;
Motor motor = Motor(EN1, IN1, IN2, EN2, IN3, IN4);

//------------------------------------------------------------------//
void setup()
{   //usb порт
  Serial.begin(9600); //скорость соединения с com портом
}

//---------------------------------------------//
void loop()
{  
 if (Serial.available() > 0) // если что-то пришло с com порта
 {    
    char cur_data_port = Serial.read();
    motor.SwitchMove(cur_data_port); // зарезервированы буквы: w, s, a, d, b
  }
}

