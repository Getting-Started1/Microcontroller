#include <DHT.h>
#include <DHT_U.h>

#define DHTPIN 7
#define DHTTYPE DHT22
//Declare DHT object:
DHT dht(DHTPIN, DHTTYPE);
//Intialize the sensor.



void setup (){
  Serial.begin(9600);
  dht.begin();
}

void loop (){
delay(10000);
//read humidity
float humi = dht.readHumidity();
//read temperature as Celsius
float tempC = dht.readTemperature();
//read temperature as Farenheit
float tempF = dht.readTemperature(true);

//check if any reads failed
if (isnan(humi) || isnan(tempC) || isnan(tempF)){
  Serial.println("Failed to read from DHT sensor!");

}else {
// Serial.print("The Temp is:");
//   Serial.print(humi);
   Serial.print("Temperature:");
  Serial.print(tempC);
  Serial.print(",");
    
 

  Serial.print("Humidity:");
  Serial.println(humi);
    // Serial.print(",");
   
 

}
}


