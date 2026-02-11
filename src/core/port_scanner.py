import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

class PortScanner:
    def __init__(self, ports, timeout=1.0, threads=100):
        self.ports = ports
        self.timeout = timeout
        self.threads = threads
        
    def scan_host(self, host):
        open_ports = []
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = {executor.submit(self._scan_port, host, port): port for port in self.ports}
            
            for future in as_completed(futures):
                port = futures[future]
                try:
                    if future.result():
                        service = self._get_service(port)
                        open_ports.append({"port": port, "service": service})
                except:
                    pass
        
        return sorted(open_ports, key=lambda x: x["port"])
    
    def _scan_port(self, host, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((host, port))
            sock.close()
            return result == 0
        except:
            return False
    
    def _get_service(self, port):
        services = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
            53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
            443: "HTTPS", 445: "SMB", 3306: "MySQL", 3389: "RDP",
            5432: "PostgreSQL", 5900: "VNC", 8080: "HTTP-Proxy"
        }
        return services.get(port, "Unknown")
