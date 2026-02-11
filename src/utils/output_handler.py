import json
import csv
from colorama import Fore

class OutputHandler:
    def __init__(self, results):
        self.results = results
        
    def print_console(self):
        print(Fore.CYAN + "\n" + "="*60)
        print(Fore.CYAN + "SCAN RESULTS".center(60))
        print(Fore.CYAN + "="*60 + "\n")
        
        for result in self.results:
            print(Fore.GREEN + f"Host: {result['host']}")
            print(Fore.YELLOW + "-" * 40)
            
            for port_info in result['open_ports']:
                print(f"  Port {port_info['port']:<6} -> {port_info['service']}")
            print()
    
    def save_to_file(self, filename, format_type):
        if format_type == "json":
            self._save_json(filename)
        elif format_type == "csv":
            self._save_csv(filename)
        else:
            self._save_txt(filename)
    
    def _save_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=4)
        print(Fore.GREEN + f"[+] Results saved to {filename}")
    
    def _save_csv(self, filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Host", "Port", "Service"])
            
            for result in self.results:
                for port_info in result['open_ports']:
                    writer.writerow([result['host'], port_info['port'], port_info['service']])
        print(Fore.GREEN + f"[+] Results saved to {filename}")
    
    def _save_txt(self, filename):
        with open(filename, 'w') as f:
            for result in self.results:
                f.write(f"Host: {result['host']}\n")
                f.write("-" * 40 + "\n")
                
                for port_info in result['open_ports']:
                    f.write(f"  Port {port_info['port']:<6} -> {port_info['service']}\n")
                f.write("\n")
        print(Fore.GREEN + f"[+] Results saved to {filename}")
