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
        scanner.scan(hosts=host, arguments='-p 1-1023 -sV -T4')

        # Print scan results for current host
        for host in scanner.all_hosts():

            print(f"Host: {host}")

            for proto in scanner[host].all_protocols():

                print(f"Protocol: {proto}")
                ports = scanner[host][proto].keys()

                for port in ports:
                    service = scanner[host][proto][port]['name']
                    state = scanner[host][proto][port]['state']
                    print(f"Port: {port}\tState: {state}\tService: {service}")

if __name__ == "__main__":
    scan_network()
