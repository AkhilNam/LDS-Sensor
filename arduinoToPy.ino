void setup() {
    Serial.begin(115200);  // Match baud rate with Python
}

void loop() {
    int sensorVal = analogRead(A5); 
    float voltage = sensorVal * (5.00 / 1023.0);  
    Serial.println(voltage, 3);  
    delay(500);  
}
