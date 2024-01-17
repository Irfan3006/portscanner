import socket
import termcolor
import pyfiglet

print(pyfiglet.figlet_format("RED--CHIKA",font="slant"))

def scan(target, ports):
    print('\n' + ' Mulai Scan Untuk ' + str(target))
    for port in range (1,ports):
        scan_port(target,port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(termcolor.colored(("[+] Port Terbuka " + str(port)), 'red'))
        sock.close()
    except:
        pass

targets = input("[*] Masukkan Target Untuk Di Scan (pisahkan dengan , (192.168.xx.xx,192.167.xx.xx,192.166.xx.xx)): ")
ports = int(input("[*] Masukkan Berapa Banyak Port Yang Akan Di Scan: "))
if ',' in targets:
        print(termcolor.colored(("[*] Scanning Beberapa Target Sekaligus"), 'green'))
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(' '), ports)
else:
        scan(targets,ports)
