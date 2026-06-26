import glob
import os
from Bio import SeqIO

def run_global_repository_audit():
    print("========================================================================")
    print("          DYNAMIC LOCAL bluePRINT REPOSITORY SCANNER (v2.0)             ")
    print("========================================================================")
    
    # Dynamically locate every file with the .fasta extension in the current folder
    fasta_files = glob.glob("*.fasta")
    
    if not fasta_files:
        print("[WARNING] No .fasta sequence manifests detected in the current directory.")
        print("Please verify this script is sitting inside your 'homo_felis_v1' folder.")
        return

    print(f"[STATUS] Located {len(fasta_files)} individual modular packages locally.\n")
    
    total_base_pairs = 0
    parsed_count = 0
    
    # Sort the files alphabetically to maintain a clean reading sequence layout
    for fasta_file in sorted(fasta_files):
        try:
            for record in SeqIO.parse(fasta_file, "fasta"):
                parsed_count += 1
                seq_length = len(record.seq)
                total_base_pairs += seq_length
                
                # Simulate transcription (DNA to RNA) for each localized file automatically
                rna_transcript = record.seq.transcribe()
                
                # Print clean, structured telemetry for the local dashboard
                print(f"File Indexed: {fasta_file:<35}")
                print(f" ├── ID:       {record.id}")
                print(f" ├── Volume:   {seq_length} base pairs")
                print(f" └── RNA Peek: {rna_transcript[:15]}...")
                print("-" * 72)
        except Exception as e:
            print(f"[ERROR] Failed to parse file {fasta_file}. Reason: {e}")
            print("-" * 72)
            
    print("\n========================================================================")
    print("                      GLOBAL COMPILE TELEMETRY                          ")
    print("========================================================================")
    print(f">> Total Modules Fully Indexed:..... {parsed_count}")
    print(f">> Consolidated Archive Volume:.... {total_base_pairs} base pairs")
    print(">> REPOSITORY STATUS:............... READY FOR HARDWARE INJECTION")
    print("========================================================================")

if __name__ == "__main__":
    run_global_repository_audit()
