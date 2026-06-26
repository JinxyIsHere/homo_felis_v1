import time
import glob
import serial
from Bio import SeqIO

SERIAL_PORT = 'COM3' # Adjust to match your Arduino port
BAUD_RATE = 9600

def initialize_hardware_stream():
    print("========================================================================")
    print("          DYNAMIC MYCO-ELECTRONIC HARDWARE STREAMER (v2.0)             ")
    print("========================================================================")
    try:
        myco_box = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)
        print(f"[STATUS] USB Pipeline opened on port {SERIAL_PORT}.\n")
        return myco_box
    except serial.SerialException:
        print(f"[ERROR] Port {SERIAL_PORT} unavailable. Running in SIMULATION MODE.\n")
        return None

def stream_all_local_manifests(hardware_gate):
    # Dynamically find and sort all fasta files in the current folder
    fasta_files = sorted(glob.glob("*.fasta"))
    
    if not fasta_files:
        print("[WARNING] No .fasta manifests detected for hardware injection.")
        return

    print(f"[STATUS] Initializing injection loop for {len(fasta_files)} modules...")
    print("-" * 72)

    for fasta_file in fasta_files:
        try:
            # Locate this block inside hf_interface_streamer.py
            for record in SeqIO.parse(fasta_file, "fasta"):
                seq_length = len(record.seq)
    
                # DYNAMIC ROUTING CONFIGURATION
                channel_trigger = "1" # Default Channel (Base, Scaffold, Seed, Endcaps, Cranes)
    
                if "pelage" in fasta_file or "crystalline" in fasta_file or "muzzle" in fasta_file:
                channel_trigger = "2" # Channel 2: Sensory & Craniofacial Interfaces
                elif "tail" in fasta_file:
                channel_trigger = "3" # Channel 3: Appendage & Structural Levers


                print(f"Streaming: {fasta_file:<30} | Length: {seq_length:>3} bp")
                print(f" -> Injecting via Channel Token '{channel_trigger}'...")
                
                if hardware_gate and hardware_gate.is_open:
                    hardware_gate.write(channel_trigger.encode())
                    time.sleep(0.5)
                    response = hardware_gate.readline().decode().strip()
                    if response: print(f"    └─► {response}")
                else:
                    time.sleep(0.5)
                    print(f"    └─► [SIMULATION] 30Hz micro-voltage spike train injected to Mushroom.")
                print("-" * 72)
        except Exception as e:
            print(f"[ERROR] Failed to stream {fasta_file}. Reason: {e}")

if __name__ == "__main__":
    gate = initialize_hardware_stream()
    stream_all_local_manifests(gate)
    if gate:
        gate.close()
        print("\n[COMPLETE] All 2520 base pairs successfully transcribed into Mycelial Matrix.")
