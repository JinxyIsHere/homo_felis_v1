// hf_myco_matrix.ino (v2.1 - P. Cubensis Stabilization Overhaul)

const int CH_FOUNDATION = 2; // Pin D2: Base, Seeds, Endcaps, Muzzle
const int CH_SENSORY    = 3; // Pin D3: Crystalline Light Pelage Fur
const int CH_APPENDAGE  = 4; // Pin D4: Prehensile Tail Switch & Core

void setup() {
  Serial.begin(9600); 
  pinMode(CH_FOUNDATION, OUTPUT);
  pinMode(CH_SENSORY, OUTPUT);
  pinMode(CH_APPENDAGE, OUTPUT);
  
  digitalWrite(CH_FOUNDATION, LOW);
  digitalWrite(CH_SENSORY, LOW);
  digitalWrite(CH_APPENDAGE, LOW);
}

void fire_stabilized_pulse_train(int target_pin, String channel_name) {
  // P. CUBENSIS MODULATION: We inject a rapid 60Hz grounding pulse right before 
  // the data stream to temporarily stabilize the fungal cell wall polarization
  for (int p = 0; p < 5; p++) {
    digitalWrite(target_pin, HIGH);
    delay(8); // 60Hz stabilization clamp
    digitalWrite(target_pin, LOW);
    delay(8);
  }
  delay(50); // Settlement buffer

  // Resume standard 30Hz biological data transcription loop
  for (int i = 0; i < 15; i++) {
    digitalWrite(target_pin, HIGH); 
    delay(16);                       
    digitalWrite(target_pin, LOW);  
    delay(17);
  }
  Serial.println("[CUBENSIS_MATRIX] " + channel_name + " Transcribed & Sealed on Pin D" + String(target_pin) + ".");
}

void loop() {
  if (Serial.available() > 0) {
    char incoming_token = Serial.read();
    switch (incoming_token) {
      case '1':
        fire_stabilized_pulse_train(CH_FOUNDATION, "FOUNDATION BLOCK (Ch1)");
        break;
      case '2':
        fire_stabilized_pulse_train(CH_SENSORY, "SENSORY BLOCK (Ch2)");
        break;
      case '3':
        fire_stabilized_pulse_train(CH_APPENDAGE, "APPENDAGE BLOCK (Ch3)");
        break;
    }
  }
}
