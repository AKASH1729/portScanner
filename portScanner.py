import socket
import termcolor
import time

def scan(target, ports):
    print('\n' + 'Starting scan for ' + str(target))
    start_time = time.time()
    for port in range(1, ports + 1):
        scan_port(target, port)
    end_time = time.time()
    print(f"\nScan completed in {end_time - start_time:.2f} seconds for {target}\n")

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)  # helps reduce waiting on unresponsive ports
        sock.connect((ipaddress, port))
        print(termcolor.colored(f"[+] Port {port} is OPEN", "green"))
        sock.close()
    except socket.timeout:
        print(termcolor.colored(f"[-] Port {port} is FILTERED (no response)", "yellow"))
    except ConnectionRefusedError:
        print(termcolor.colored(f"[-] Port {port} is CLOSED", "red"))
    except Exception as e:
        print(termcolor.colored(f"[!] Port {port}: Error - {e}", "magenta"))

targets = input("[+] Enter the target(s) to scan (split by ','): ")
ports = int(input("[+] Enter how many ports you want to scan (e.g. 1000): "))

if ',' in targets:
    print(termcolor.colored("[*] Scanning multiple targets", "cyan"))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(), ports)
else:
    scan(targets.strip(), ports)

