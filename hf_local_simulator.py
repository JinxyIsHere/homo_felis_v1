# hf_local_simulator.py
import os
import random
import time
from datetime import datetime
from Bio import SeqIO

class LocalSandboxCrawler:
    def __init__(self, crawler_id):
        self.crawler_id = crawler_id
        self.log_file = "crawler_patrol.log"
        self.observation_queue = []
        self.token_bucket = 0
        self.bucket_threshold = 100
        self.fill_rate = 50

    def log_event(self, event_type, message):
        """Appends a local timestamped entry to the persistent log file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] [{event_type}] [SIMULATOR_{self.crawler_id}] {message}\n"
        with open(self.log_file, "a") as f:
            f.write(log_line)

    def execute_pure_software_sweep(self, folder="."):
        print("\n========================================================================")
        print(f"      OFFLINE SANDBOX SIMULATOR: INITIALIZING RECURSIVE RECON         ")
        print("========================================================================")
        self.log_event("INFO", "Starting offline software-only repository validation sweep.")
        
        self.observation_queue = []
        fasta_files = [f for f in os.listdir(folder) if f.endswith('.fasta')]
        print(f"[STATUS] Canyoning directory... Found {len(fasta_files)} .fasta manifests.")
        print("-" * 72)
        
        total_bp = 0
        for fasta_file in sorted(fasta_files):
            try:
                for record in SeqIO.parse(os.path.join(folder, fasta_file), "fasta"):
                    seq_len = len(record.seq)
                    total_bp += seq_len
                    self.log_event("AUDIT_PASS", f"Verified file: {fasta_file} | Size: {seq_len} bp")
                    print(f"Auditing Manifest: {fasta_file:<30} | Length: {seq_len:>3} bp")
                    
                    # 2% chance to simulate catching an unscheduled environmental mutation artifact offline
                    if random.random() < 0.02:
                        faulty_idx = random.randint(0, seq_len - 1)
                        print(f" >> [ALERT] Unscheduled anomaly isolated in {fasta_file} at pos {faulty_idx}!")
                        self.log_event("SECURITY_ALERT", f"Isolated mutation in {fasta_file} at position {faulty_idx}.")
                        self.observation_queue.append({
                            "file": fasta_file,
                            "pos": faulty_idx,
                            "diagnosis": "Cosmic Ray Inversion / Base-Pair Drift"
                        })
                        time.sleep(0.2)
            except Exception as e:
                self.log_event("CRITICAL_ERROR", f"Failed parsing on {fasta_file}: {e}")

        print("-" * 72)
        print(f">> Consolidated Active Volume Verified: {total_bp} base pairs.")
        self.log_event("INFO", f"Sweep complete. Local repository baseline clocked at {total_bp} bp.")
        return total_bp

    def simulate_manual_review_gate(self):
        print(f"\n[ALERT] Isolated items in Staging Observation Queue: {len(self.observation_queue)}")
        for idx, item in enumerate(self.observation_queue, 1):
            print(f" ├── ANOMALY {idx:02d}: File: {item['file']} | Position: {item['pos']}")
            print(f" └── Diagnosis:  {item['diagnosis']} [SILENCED & QUARANTINED]")
        
        print("\n[INTERFACE] Simulated Human-In-The-Loop (HITL) Gate Locked.")
        print("Instructions: Type 'ACTION' and press Enter to simulate authorization handshake.")
        
        start = time.time()
        user_key = input("[KEY TERMINAL] waiting for admin confirmation... ")
        end = time.time()
        
        tokens = (end - start) * self.fill_rate
        if user_key.upper() == "ACTION" and tokens >= self.bucket_threshold:
            print("\n------------------------------------------------------------------------")
            print(f">> INTERNAL NEURAL PULSE:........... VERIFIED ({int(tokens)} Tokens accumulated)")
            print(">> EXTERNAL HAPTIC PATCH:........... VERIFIED [Simulated Haptic Click]")
            print(">> REPOSITORY INJECTION STATUS:..... GRANTED (SIMULATED PIPELINE PASS)")
            print("------------------------------------------------------------------------")
            self.log_event("HANDSHAKE", "Access Granted. Local simulation sandbox successfully compiled.")
        else:
            print("\n[DENIED] Handshake failed or timeout broken. Main branch preserved in read-only stasis.")
            self.log_event("HANDSHAKE", "Access Denied. Intent mismatch or focus timeout break.")

if __name__ == "__main__":
    simulator = LocalSandboxCrawler("BETA_02")
    total_volume = simulator.execute_pure_software_sweep()
    simulator.simulate_manual_review_gate()
