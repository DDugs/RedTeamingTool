import nmap

def scan_network(ip_range):
    nm = nmap.PortScanner()
    nm.scan(ip_range, arguments='-sV -O')  # Added -O for OS detection

    targets = []
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            services = nm[host].all_protocols()
            open_ports = []
            if 'tcp' in services:
                open_ports = nm[host]['tcp'].keys()  # Get open TCP ports
            
            # Collect OS information if available
            os_info = nm[host].get('osclass', [{}])[0].get('osfamily', 'unknown')  # Default to 'unknown'
            
            target_info = {
                'ip': host,
                'ports': open_ports,
                'os': os_info  # Store OS information
            }
            targets.append(target_info)

    return targets  # Return the list of targets


# Based on the services, decide on the type of attack
def choose_attack(target):
    # Ensure target is a dictionary
    if isinstance(target, dict):
        open_ports = target.get('ports', [])
        if 22 in open_ports:
            print("SSH Service Found. Launching SSH Attack.")
        elif 445 in open_ports:
            print("SMB Service Found. Attempting SMB-based attack.")
    else:
        print(f"Invalid target format: {target}")

