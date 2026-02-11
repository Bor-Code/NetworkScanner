import sys
import os
from src.cli.arguments import parse_arguments
from src.core.scanner import NetworkScanner
from src.utils.output_handler import OutputHandler
from colorama import init, Fore

init(autoreset=True)

def main():
    print(Fore.CYAN + """
    ╔═══════════════════════════════════════╗
    ║     Network Scanner v1.0              ║
    ║     Cross-Platform Network Tool       ║
    ╚═══════════════════════════════════════╝
    """)
    
    args = parse_arguments()
    
    try:
        scanner = NetworkScanner(
            target=args.target,
            ports=args.ports,
            threads=args.threads,
            timeout=args.timeout
        )
        
        results = scanner.execute_scan()
        
        output_handler = OutputHandler(results)
        
        if args.output:
            output_handler.save_to_file(args.output, args.format)
        else:
            output_handler.print_console()
            
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Scan interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(Fore.RED + f"[!] Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
