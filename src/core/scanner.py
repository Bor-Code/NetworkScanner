import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from src.utils.network_utils import parse_target, parse_ports, check_privileges
from src.core.host_discovery import HostDiscovery
from src.core.port_scanner import PortScanner
from colorama import Fore

class NetworkScanner:
    def __init__(self, target, ports, threads=100, timeout=1.0):
        self.target = target
        self.ports = parse_ports(ports)
        self.threads = threads
        self.timeout = timeout
        self.results = []
        
    def execute_scan(self):
        print(Fore.YELLOW + f"[*] Starting scan on {self.target}")
        print(Fore.YELLOW + f"[*] Scanning {len(self.ports)} ports with {self.threads} threads\n")
        
        ip_list = parse_target(self.target)
        
        host_discovery = HostDiscovery(self.timeout)
        active_hosts = host_discovery.discover_hosts(ip_list)
        
        if not active_hosts:
            print(Fore.RED + "[!] No active hosts found")
            return []
        
        print(Fore.GREEN + f"[+] Found {len(active_hosts)} active hosts\n")
        
        port_scanner = PortScanner(self.ports, self.timeout, self.threads)
        
        for host in active_hosts:
            print(Fore.CYAN + f"[*] Scanning {host}...")
            open_ports = port_scanner.scan_host(host)
            
            if open_ports:
                self.results.append({
                    "host": host,
                    "open_ports": open_ports
                })
                print(Fore.GREEN + f"[+] {host}: {len(open_ports)} open ports")
            else:
                print(Fore.YELLOW + f"[-] {host}: No open ports")
        
        return self.results
