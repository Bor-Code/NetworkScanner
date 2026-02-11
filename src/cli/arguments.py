import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Professional Network Scanner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  netscan -t 192.168.1.0/24
  netscan -t 192.168.1.1 -p 80,443,8080
  netscan -t 10.0.0.0/24 -p 1-1000 -o results.json
        """
    )
    
    parser.add_argument(
        "-t", "--target",
        required=True,
        help="Target IP address or CIDR range (e.g., 192.168.1.0/24)"
    )
    
    parser.add_argument(
        "-p", "--ports",
        default="21,22,23,25,80,443,445,3389,8080",
        help="Ports to scan (e.g., 80,443 or 1-1000)"
    )
    
    parser.add_argument(
        "-T", "--threads",
        type=int,
        default=100,
        help="Number of threads (default: 100)"
    )
    
    parser.add_argument(
        "--timeout",
        type=float,
        default=1.0,
        help="Timeout for each connection (default: 1.0)"
    )
    
    parser.add_argument(
        "-o", "--output",
        help="Output file path"
    )
    
    parser.add_argument(
        "-f", "--format",
        choices=["json", "csv", "txt"],
        default="txt",
        help="Output format (default: txt)"
    )
    
    parser.add_argument(
        "--arp",
        action="store_true",
        help="Use ARP scanning (requires root/admin)"
    )
    
    return parser.parse_args()
