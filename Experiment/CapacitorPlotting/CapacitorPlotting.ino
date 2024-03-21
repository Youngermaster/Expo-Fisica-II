int ValorSensor = 0;  
void setup() 
{
  Serial.begin(9600);
  while(!Serial) {}
}
void loop() 
{
  ValorSensor = analogRead(A0);
  Serial.println(ValorSensor);
  delay(100);
}
