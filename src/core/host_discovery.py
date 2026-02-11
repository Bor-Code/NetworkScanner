import socket
import platform
import subprocess
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore

class HostDiscovery:
    def __init__(self, timeout=1.0):
        self.timeout = timeout
        
    def discover_hosts(self, ip_list):
        active_hosts = []
        
        with ThreadPoolExecutor(max_workers=50) as executor:
            futures = {executor.submit(self._ping_host, ip): ip for ip in ip_list}
            
            for future in futures:
                if future.result():
                    active_hosts.append(futures[future])
        
        return active_hosts
    
    def _ping_host(self, ip):
        try:
            param = "-n" if platform.system().lower() == "windows" else "-c"
            command = ["ping", param, "1", "-w" if platform.system().lower() == "windows" else "-W", "1", ip]
            
            result = subprocess.run(
                command,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=self.timeout
            )
            return result.returncode == 0
        except:
            return False
