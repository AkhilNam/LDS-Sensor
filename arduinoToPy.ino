void setup() {
    Serial.begin(115200);  // Match baud rate with Python
}

void loop() {
    int sensorVal = analogRead(A5); 
    float voltage = sensorVal * (5.0 / 1023.0);  
    Serial.println(voltage);  
    delay(500);  
}
