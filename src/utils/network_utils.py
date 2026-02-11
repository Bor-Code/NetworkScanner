import ipaddress
import os

def parse_target(target):
    try:
        network = ipaddress.ip_network(target, strict=False)
        return [str(ip) for ip in network.hosts()]
    except ValueError:
        return [target]

def parse_ports(port_string):
    ports = []
    
    for part in port_string.split(","):
        if "-" in part:
            start, end = map(int, part.split("-"))
            ports.extend(range(start, end + 1))
        else:
            ports.append(int(part))
    
    return sorted(set(ports))

def check_privileges():
    return os.geteuid() == 0 if hasattr(os, 'geteuid') else True
