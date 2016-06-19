class Motor
{
  public:
    Motor(int _EN1, int _IN1, int _IN2, int _EN2, int _IN3, int _IN4)
    ~Motor();  
    
    int EN1, IN1, IN2, EN2, IN3, IN4;
}

Motor::Motor(int _EN1, int _IN1, int _IN2, int _EN2, int _IN3, int _IN4)
{
  EN1 = _EN1;
  IN1 = _IN1;
  IN2 = _IN2;
  EN2 = _EN2;
  IN3 = _IN3;
  
}

Motor a = Motor(3, 2, 5, 6, 7, 8);
a.EN1
