import time
import serial
from Bio import SeqIO
# Import your background file-logging crawler unit directly
from hf_security_crawler import LiveGenomicCrawler

# ========================================================================
# HARDWARE CONFIGURATION
# Adjust 'COM3' (Windows) or '/dev/tty.usbmodem...' (Mac/Linux) to match your Arduino port
# ========================================================================
SERIAL_PORT = 'COM3'
BAUD_RATE = 9600

class FullyIntegratedAdminDashboard:
    def __init__(self):
        self.epoch_id = "EPOCH_01_GATE"
        self.token_bucket = 0
        self.bucket_threshold = 100
        self.fill_rate = 50   
        self.security_node = LiveGenomicCrawler(crawler_id="ALPHA_01")
        self.observation_queue = []
        self.hardware_gate = self.initialize_myco_connection()

    def initialize_myco_connection(self):
        """Opens a direct USB connection to the local Mycelial Interface Box."""
        try:
            myco_box = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
            time.sleep(2) # Handshake buffer time
            print(f"[STATUS] Connected to physical Mycelial Interface on port {SERIAL_PORT}.")
            return myco_box
        except serial.SerialException:
            print(f"[STATUS] Port {SERIAL_PORT} offline. Dashboard running in SIMULATION/SANDBOX MODE.")
            return None

    def load_live_telemetry_stream(self):
        print("\n========================================================================")
        print(f"     HOMO-FELIS INDUSTRIAL RECON DASHBOARD: {self.epoch_id}           ")
        print("========================================================================")
        print(">> CHASSIS BASELINE RUNTIME:......... ONLINE [Homo-Felis v1.2]")
        
        # Run background scanner and dump telemetry to 'crawler_patrol.log'
        self.observation_queue = self.security_node.run_recursive_integrity_sweep()
        
        is_stable = self.security_node.evaluate_tri_channel_safety()
        stress_status = "14% [Optimal Eustress]" if is_stable else "OVERFLOW CRITICAL"
        
        print(f">> ADAPTIVE STRESS CONTAINER:........ {stress_status}")
        print(">> STASIS BUFFER:.................... ACTIVE [Pipeline Soft-Paused]")
        print("========================================================================")

    def render_observation_queue(self):
        print(f"\n[ALERT] {len(self.observation_queue) + 1} Items Isolated for Manual Review:")
        print("-" * 72)
        print("ITEM 01: [VARIANCE ZONE - MANUALLY QUARANTINED]")
        print(" ├── Source File:  hf_dental_matrix.fasta (240 bp)")
        print(" ├── Diagnosis:    Mastication Glitch. Conflict between Molars and Carnassials.")
        print(" └── Status:       FROZEN. Awaiting Top-Down Admin Target Selection.")
        print("-" * 72)
        
        item_id = 2
        for anomaly in self.observation_queue:
            print(f"ITEM {item_id:02d}: [CRAWLER INTERCEPT - UNSCHEDULED VARIATION]")
            print(f" ├── Source File:  {anomaly['file']} ({anomaly['id']})")
            print(f" ├── Coordinates:  Nucleotide Position {anomaly['pos']}")
            print(f" └── Status:       {anomaly['status']}. Logged to persistent text file.")
            print("-" * 72)
            item_id += 1

    def dispatch_hardware_pulse_train(self, channel_token):
        """Sends the exact channel trigger byte down the USB line to execute the 30Hz train."""
        if self.hardware_gate and self.hardware_gate.is_open:
            print(f" -> Pulsing Fungal Network over channel token '{channel_token}'...")
            self.hardware_gate.write(channel_token.encode())
            time.sleep(0.5)
            response = self.hardware_gate.readline().decode().strip()
            if response:
                print(f"    └─► {response}")
        else:
            print(f" -> [SIMULATION] 30Hz micro-voltage pulse train injected via Channel {channel_token}.")

    def execute_handshake(self, action_name):
        print(f"\n[SYSTEM] Preparing sequence execution for command: [{action_name}]")
        print("Instructions: Type 'ACTION' and press Enter to complete the physical key input.")
        
        start_time = time.time()
        user_input = input("\n[KEY TERMINAL] waiting for token authorization... ")
        end_time = time.time()
        
        elapsed = end_time - start_time
        accumulated = elapsed * self.fill_rate
        
        if user_input.upper() == "ACTION" and accumulated >= self.bucket_threshold:
            self.token_bucket = min(accumulated, self.bucket_threshold)
            print("\n------------------------------------------------------------------------")
            print(f">> INTERNAL NEURAL PULSE:........... VERIFIED ({int(self.token_bucket)} Tokens)")
            print(">> EXTERNAL HAPTIC PATCH:........... VERIFIED [Synchronized Haptic Click]")
            print(">> STATUS:.......................... HANDSHAKE MATCH: ACCESS GRANTED")
            print("------------------------------------------------------------------------")
            return True
        else:
            print("\n[ERROR] Handshake failed. System returned to safe read-only stasis buffer.")
            return False

    def launch_interface(self):
        self.load_live_telemetry_stream()
        self.render_observation_queue()
        
        print("\nSelect Administrator Action:")
        print(" 1. Authorize & Inject Hybridized Omnivore Dental Package (Item 01)")
        print(" 2. Execute Apoptosis Cleanup on all Crawler Anomalies (Items 02+)")
        print(" 3. Exit Dashboard (Maintain Soft Pause Status)")
        
        user_choice = input("\n[ADMIN INPUT] Select option (1-3): ")
        
        if user_choice == "1":
            if self.execute_handshake("MERGE_HYBRID_TEETH"):
                print("\n[INJECTION] Streaming dental block configuration to hardware...")
                # Channel 1 maps to structural bone/teeth arrays on your Arduino configuration
                self.dispatch_hardware_pulse_train("1")
                print("[SUCCESS] All files merged. Insulator caps released.")
        elif user_choice == "2":
            if len(self.observation_queue) == 0:
                print("\n[INFO] No crawler anomalies detected. Observation path clear.")
            else:
                if self.execute_handshake("CLEAR_UNSCHEDULED_MUTATIONS"):
                    print("\n[INJECTION] Deploying emergency counter-measures down hardware lines...")
                    # Pulse the network to signal a localized cleanup sweep
                    self.dispatch_hardware_pulse_train("1")
        else:
            print("\nExiting dashboard. Soft pause maintained. All blocks frozen safely.")
            
        if self.hardware_gate:
            self.hardware_gate.close()

if __name__ == "__main__":
    dashboard = FullyIntegratedAdminDashboard()
    dashboard.launch_interface()