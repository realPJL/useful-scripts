# DISCLAIMER:   This script is intended for educational and legitimate network administration purposes only. Unauthorized use of this script for malicious activities is strictly prohibited. By using this script, you agree to use it responsibly and in compliance with applicable laws and regulations.
# WARNING:      Unauthorized access to computer networks and systems may violate local, state, federal, and international laws. It is your responsibility to ensure that you have appropriate authorization before scanning or accessing any network or system. The author of this script disclaims any liability for unauthorized or illegal use.

# pip install python-nmap
import nmap
import logging

# Logging config
logging.basicConfig(filename='log_scan_network.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scan_network():    
    scanner = nmap.PortScanner()

    logging.info("Scanning for live hosts...")
    scanner.scan(hosts= target_network, arguments='-sn')    # -sn -> ping sweep without attempting to port scan the host (sends ICMP Echo Request ping)

    # List of all hosts that responded to ping
    live_hosts = [x for x in scanner.all_hosts() if scanner[x]['status']['state'] == 'up']

    # Perform detailed port scan on each live host
    for host in live_hosts:

        logging.info(f"Scanning host {host}...")
        # -p    specifies range of ports to scan
        # -sV   perform version detection
        # -T4   sets timing template to aggressive
        # -O    operating system detection
        # -sC   script scanning
        scan_arguments = '-p 1-1023 -O -sV -sC -T4 --script vuln'
        logging.info(f"Scan command: nmap {host} {scan_arguments}")
        scanner.scan(hosts=host, arguments=scan_arguments)


        # Print scan results for current host
        logging.info(f"Results for host {host}: ")
        for host in scanner.all_hosts():
            logging.info(f"Host:   {host}")

            if 'osmatch' in scanner[host]:
                logging.info("Operating System:")
                for os_match in scanner[host]["osmatch"]:
                    logging.info(f"- {os_match['name']} (Accuracy: {os_match['accuracy']})")
            
            if 'scripts' in scanner[host]:
                logging.info("Script Scan Results:")
                for script_id, script_result in scanner[host]['scripts'].items():
                    logging.info(f"- {script_id}:  {script_result['output']}")

            for proto in scanner[host].all_protocols():
                logging.info(f"Protocol: {proto}")
                ports = scanner[host][proto].keys()

                for port in ports:
                    service = scanner[host][proto][port]['name']
                    state = scanner[host][proto][port]['state']
                    logging.info(f"Port: {port}\tState: {state}\tService: {service}")

                    if 'product' in scanner[host][proto][port]:
                        product = scanner[host][proto][port]['product']
                        logging.info(f"Service Banner: {product}")

                    # Check if vulnerability scan results are available for the port
                    if 'script' in scanner[host][proto][port]:
                        vulnerability_scripts = scanner[host][proto][port]['script']

                        if 'vulners' in vulnerability_scripts:
                            logging.info("Vulnerability Scan Results:")

                            vuln_result = ""

                            for vulnerability_script in vulnerability_scripts['vulners']:
                                vuln_result += vulnerability_script
                            logging.info(vuln_result)
                            
                        else:
                            logging.info("No vulnerability scan results available.")
                    else:
                        logging.info("No vulnerability scan results available.")

def print_results_to_console():
    if print_results == 'y':
        with open('log_scan_network.txt', 'r') as f:
            file_content = f.read()
        print(file_content)
    elif print_results == 'n':
        print('The script closes now. You can see the results in the log_scan_network.txt file.')


if __name__ == "__main__":
    target_network = input("Enter the target network or IP range to scan: ")        # localhost / loopback = 127.0.0.0/8
    scan_network()
    print("Scan results saved in log_scan_network.txt")
    print_results = input("Do you want to print them out here? (y,n): ")
    print_results_to_console()
