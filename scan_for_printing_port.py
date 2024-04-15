import socket

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Adjust timeout as needed
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} on {target} is open")
        sock.close()
    except KeyboardInterrupt:
        print("Scan interrupted.")
    except socket.error:
        print("Socket error occurred.")

def scan_printer(target):
    print(f"Scanning printer on {target}")
    scan_port(target, 631)

if __name__ == "__main__":
    # Replace "127.0.0.1" with the IP address of the printer you want to scan
    target = "127.0.0.1"
    scan_printer(target)
