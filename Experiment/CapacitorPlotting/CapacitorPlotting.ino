// Variable para almacenar el valor leído del sensor
int ValorSensor = 0;
// Variable para almacenar el tiempo desde que el Arduino empezó a ejecutarse
unsigned long tiempo;

void setup() 
{
  Serial.begin(9600);
  while(!Serial) {}
}

void loop() 
{
  // Obtiene el tiempo actual en milisegundos
  tiempo = millis();

  // Lee el valor del pin A0 y lo almacena en la variable ValorSensor
  ValorSensor = analogRead(A0);

  // Envía el valor leído y el tiempo transcurrido al Monitor Serial
  // Formato: tiempo,ValorSensor
  Serial.print(tiempo);
  Serial.print(",");
  Serial.println(ValorSensor);

  // Espera 100 milisegundos antes de leer el siguiente valor
  delay(100);
}
