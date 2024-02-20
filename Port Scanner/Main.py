import socket
from termcolor import colored

def scan(target,ports):
    print('\n' + '*** Starting Scan For' + str(target) + ' ***')
    for port in range(1, ports):
        scan_port(target, port)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.3)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + ' :' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ' +str(port))
        sock.close()
    except:
        pass

targets = input('[+] Enter target To Scan: ')
ports = int(input('[+] Enter How Many Ports You Want To Scan: '))
if ',' in targets:
    print(colored(("\n[*] Scanning Multiple targets [*]\n"), 'green'))
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '),ports)
else:
    scan(targets,ports)
