long rnd1;
long rnd2;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  randomSeed(analogRead(0));
}

void loop() {
  // put your main code here, to run repeatedly:
  rnd1 = random(100);

  rnd2 = random(100);
  
  Serial.println((String)rnd1+";"+(String)rnd2);

  delay(1000);

}