# DISCLAIMER:   This script is intended for educational and legitimate network administration purposes only. Unauthorized use of this script for malicious activities is strictly prohibited. By using this script, you agree to use it responsibly and in compliance with applicable laws and regulations.
# WARNING:      Unauthorized access to computer networks and systems may violate local, state, federal, and international laws. It is your responsibility to ensure that you have appropriate authorization before scanning or accessing any network or system. The author of this script disclaims any liability for unauthorized or illegal use.

# pip install python-nmap
import nmap

def scan_network():    
    scanner = nmap.PortScanner()

    print("Scanning for live hosts...")
    scanner.scan(hosts='127.0.0.1', arguments='-sn')    # -sn -> ping sweep without attempting to port scan the host (sends ICMP Echo Request ping)

    # List of all hosts that responded to ping
    live_hosts = [x for x in scanner.all_hosts() if scanner[x]['status']['state'] == 'up']

    # Perform detailed port scan on each live host
    for host in live_hosts:

        print(f"Scanning host {host}...")
        # -p    specifies range of ports to scan
        # -sV   perform version detection
        # -T4   sets timing template to aggressive
        # -O    operating system detection
        # -sC   script scanning
        scan_arguments = '-p 1-1023 -O -sV -sC -T4'
        print(f"Scan command: nmap {host} {scan_arguments}")
        scanner.scan(hosts=host, arguments=scan_arguments)

        # Print scan results for current host
        print(f"Results for host {host}: ")
        for host in scanner.all_hosts():
            print(f"Host:   {host}")

            if 'osmatch' in scanner[host]:
                print("Operating System:")
                for os_match in scanner[host]["osmatch"]:
                    print(f"- {os_match['name']} (Accuracy: {os_match['accuracy']})")
            
            if 'scripts' in scanner[host]:
                print("Script Scan Results:")
                for script_id, script_result in scanner[host]['scripts'].items():
                    print(f"- {script_id}:  {script_result['output']}")

            for proto in scanner[host].all_protocols():
                print(f"Protocol: {proto}")
                ports = scanner[host][proto].keys()

                for port in ports:
                    service = scanner[host][proto][port]['name']
                    state = scanner[host][proto][port]['state']
                    print(f"Port: {port}\tState: {state}\tService: {service}")

if __name__ == "__main__":
    scan_network()
