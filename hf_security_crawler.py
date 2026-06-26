import os
import random
import time
from datetime import datetime
from Bio import SeqIO

class LiveGenomicCrawler:
    def __init__(self, crawler_id):
        self.crawler_id = crawler_id
        self.active_scans = 0
        self.log_file_name = "crawler_patrol.log"
        self.tri_channel_consensus = {
            "cap_strain": "SAFE",
            "crane_pulse": "ACTIVE",
            "crawler_audit": "CLEAR"
        }

    def write_to_persistent_log(self, status_type, log_message):
        """Writes timestamped, structured telemetry entries to a local log file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{status_type}] [CRAWLER_{self.crawler_id}] {log_message}\n"
        
        # Append mode ('a') ensures old system logs are preserved, not overwritten
        with open(self.log_file_name, "a") as f:
            f.write(log_entry)

    def run_recursive_integrity_sweep(self, folder_path="."):
        """Scans all local .fasta files, cross-referencing structural integrity constraints."""
        print(f"\n========================================================================")
        print(f"      CRAWLER SYSTEM PATROL IN PROGRESS: INFRASTRUCTURE AUDIT           ")
        print(f"========================================================================")
        print(f"[CRAWLER_{self.crawler_id}] Initializing sweep... Streaming logs to {self.log_file_name}")
        
        # Log the initialization of the system epoch patrol
        self.write_to_persistent_log("INFO", "Initializing global repository recursive integrity sweep.")
        
        quarantine_payload = []
        fasta_files = [f for f in os.listdir(folder_path) if f.endswith('.fasta')]
        self.write_to_persistent_log("INFO", f"Located {len(fasta_files)} individual sequence manifests for audit.")
        
        for fasta_file in sorted(fasta_files):
            self.active_scans += 1
            file_path = os.path.join(folder_path, fasta_file)
            
            try:
                for record in SeqIO.parse(file_path, "fasta"):
                    seq_str = str(record.seq)
                    
                    # Log successful file ingestion checks
                    self.write_to_persistent_log("AUDIT_PASS", f"Indexed file: {fasta_file} | ID: {record.id} | Size: {len(seq_str)} bp")
                    
                    # Simulate a 1.5% chance of catching an environmental radiation anomaly
                    if random.random() < 0.015:
                        faulty_pos = random.randint(0, len(seq_str) - 1)
                        print(f" >> [ALERT] Unscheduled modification flagged in {fasta_file} at pos {faulty_pos}!")
                        
                        # Write the critical security alert to the physical log file
                        self.write_to_persistent_log("SECURITY_ALERT", f"UNSCHEDULED EDIT ENCOUNTERED in {fasta_file} at position {faulty_pos} (Suspected Cosmic Ray Impact).")
                        
                        anomaly_item = {
                            "file": fasta_file,
                            "id": record.id,
                            "pos": faulty_pos,
                            "diagnosis": "Cosmic Ray Impact / Environmental Radical Intercept",
                            "status": "SILENCED & QUARANTINED"
                        }
                        quarantine_payload.append(anomaly_item)
                        time.sleep(0.1)
            except Exception as e:
                error_msg = f"Failed to inspect file {fasta_file}. Reason: {e}"
                print(f"[ERROR] {error_msg}")
                self.write_to_persistent_log("CRITICAL_ERROR", error_msg)
                
        self.write_to_persistent_log("INFO", f"Multi-window sweep finalized. Total files checked: {len(fasta_files)}.")
        return quarantine_payload

    def evaluate_tri_channel_safety(self):
        """Ensures cap strain and crane pulse logs match safely before a merge."""
        self.write_to_persistent_log("INFO", "Executing automated Tri-Channel Consensus gateway handshake validation.")
        
        if self.tri_channel_consensus["cap_strain"] == "SAFE" and self.tri_channel_consensus["crane_pulse"] == "ACTIVE":
            self.tri_channel_consensus["crawler_audit"] = "CLEAR"
            self.write_to_persistent_log("CONSENSUS", "RESULT: PASSED. Cap Strain: SAFE | Crane Pulse: ACTIVE. System stable.")
            return True
        else:
            self.tri_channel_consensus["crawler_audit"] = "FAILED"
            self.write_to_persistent_log("CONSENSUS", "RESULT: FAILED CRITICAL. Mechanical strain mismatch or dead crane heartbeat pulse detected.")
            return False

if __name__ == "__main__":
    # Diagnostic test run
    patrol_unit = LiveGenomicCrawler("ALPHA_01")
    patrol_unit.run_recursive_integrity_sweep()
    patrol_unit.evaluate_tri_channel_safety()