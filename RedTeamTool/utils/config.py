ATTACK_MAPPING = {
    "reconnaissance": "T1071",
    "privilege_escalation": "T1068",
    "persistence": "T1053",
    "lateral_movement": "T1021",
}

def map_to_mitre(tactic):
    return ATTACK_MAPPING.get(tactic, "Unknown Tactic")

# Example Usage
tactic = "reconnaissance"
print(f"Reconnaissance maps to MITRE ATT&CK ID: {map_to_mitre(tactic)}")
