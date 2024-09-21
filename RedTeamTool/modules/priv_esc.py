import subprocess

def run_linpeas():
    subprocess.run(["./linpeas.sh"], shell=True)
    print("Running LinPEAS for privilege escalation checks")

def windows_priv_esc():
    print("Attempting to exploit PrintNightmare (CVE-2021-34527)")
    # Your exploitation script for PrintNightmare vulnerability
    subprocess.run(["exploit/windows/local/printnightmare"], shell=True)
    
def linux_priv_esc():
    print("Attempting Linux privilege escalation...")
    # Add additional Linux-specific escalation techniques here
    run_linpeas()  # Running LinPEAS as part of Linux privilege escalation

