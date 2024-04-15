# Thanks to ChatGPT for the idea (and some code :D)
import socket

def scan_ports(target, start_port, end_port):
    print(f"Scanning target: {target}")
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Adjust timeout as needed
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
            sock.close()
        except KeyboardInterrupt:
            print("Scan interrupted.")

# Loopback address for local computer - just replace it with the target IP adress you want to scan
target = "127.0.0.1"
start_port = 1
end_port = 1023

# Ports 0 - 1023        = System Ports
# Ports 1024 - 49.151   = User Ports
# Ports 49.152 - 65.535 = Dynamic Ports

scan_ports(target, start_port, end_port)
