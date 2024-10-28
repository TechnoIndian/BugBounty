import os, time, ipaddress, socket, base64, zlib, sys, subprocess, argparse
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from .Bug_Bounty import BugBounty

DEFAULT_TIMEOUT = 1
EXCLUDE_LOCATION = 'https://jio.com/BalanceExhaust'

# ANSI color
os.system('clear')
y, c, g, pr, lb, r, rd, rkj, rkk = '\033[1m\033[33m', '\033[1m\033[96m', '\033[1m\033[92m', '\033[1m\033[35m', '\033[1m\033[94m', '\033[0m', '\033[1m\033[91m', '\033[1m\033[38;5;202m', '\033[1m\033[38;5;27m'

# Check and install required modules
try:
    import requests
except ImportError:
    print(f"{lb}[ {pr}* {lb}] {c} Installing requests module...{g}\n")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests
    os.system('clear')

def get_hosts_from_file(file_path):
    hosts = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                if '/' in line:
                    hosts.extend(get_hosts_from_cidr(line))
                else:
                    hosts.append(line)
    except (OSError, ValueError) as e:
        print(f'Error reading file: {e}')
    return hosts

def get_hosts_from_cidr(cidr):
    try:
        network = ipaddress.ip_network(cidr, strict=False)
        return [str(ip) for ip in network.hosts()]
    except ValueError as e:
        print(f'\n{lb}[ {rd}Error {lb}]{rd} Invalid IP-Range/CIDR input: {e} ✘{r}\n')
        return []

def enable_wake_lock():
    subprocess.run(['termux-wake-lock'])

def format_row(ip, code, server, port, host, location=None, color=r):
    row = c if 'CloudFront' in server else g if 'cloudflare' in server else y if 'AkamaiGHost' in server else y if 'AkamaiNetStorage' in server else lb if 'Varnish' in server else None
    ip_color = server_color = port_color = code_color = host_color = L_C = row or r
    L_C = g if not row else L_C
    L_D = f' -> {L_C}{location}{rd}' if location else ''
    return (f'{ip_color}{ip:<15}  {code:<6} {server_color}{server:<23}'
            f'{port_color}{port:<5}   {host_color}{host}{L_D}{rd}')

def get_ip_addresses(host):
    try:
        return socket.gethostbyname_ex(host)[2]
    except socket.gaierror:
        return []

def check_http_response(host, port):
    url = f'http://{host}:{port}' if port != '443' else f'https://{host}:{port}'
    try:
        response = requests.request('GET', url, timeout=DEFAULT_TIMEOUT, allow_redirects=False)
        IP = get_ip_addresses(host)
        if EXCLUDE_LOCATION in response.headers.get('Location', ''):
            return None
        S_H = response.headers.get('Server', '')
        location = response.headers.get('Location')
        R_S = response.status_code
        
        R_S = f"{pr}{R_S:<6}" if location and location.startswith(f"https://{host}") else R_S

        return R_S, S_H, port, host, IP, location
    except requests.exceptions.RequestException:
        return None


def format_time(elapsed_time):
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    return f'{hours:02}h:{minutes:02}m:{seconds:02}s'
    
def is_ip_address(host):
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False
        
def perform_scan(hosts, ports, output_file, threads, is_ip_only_mode=False, cidr_mode=False):
    os.system('clear')
    print(format_row('IP Address', 'Code', 'Server', 'Port', 'Host', r))
    print(' ---------------  ----  ----------------       -----  ------------------------------')
    total_hosts = len(hosts) * len(ports)
    scanned_hosts, responded_hosts = 0, 0
    start_time = time.time()
    cloudflare_hosts, cloudfront_hosts = {}, {}
    other_responds = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(check_http_response, host, port): (host, port) for host in hosts for port in ports}
        for future in as_completed(futures):
            scanned_hosts += 1
            result = future.result()
            if result:
                responded_hosts += 1
                code, server, port, host, IP, location = result
                print(format_row(IP[0], code, server, port, host, location))
                
                if 'cloudflare' in server:
                    cloudflare_hosts.setdefault(host, []).extend(IP)
                elif 'CloudFront' in server:
                    cloudfront_hosts.setdefault(host, []).extend(IP)
                else:
                    other_responds.append((IP[0], code, server, host))

            progress_line = f"[{c} PC - {pr}{(scanned_hosts / total_hosts) * 100:.3f}% {c}SN - {pr}{scanned_hosts}/{y}{total_hosts} - {c}Responded - {g}{responded_hosts} {pr}< {format_time(time.time() - start_time)} > ]"
            print(progress_line, end='\r')

    print(f'\n\n{c}Working Hosts saved to: {g}︻デ═一 {y}{output_file}{r}\n\n{r}_____________________________________________________________\n')

    with open(output_file, 'w') as file:
        for response in other_responds:
            ip, code, server, host = response
        
            if is_ip_address(host):
                file.write(f"{ip} | {server} | {code}\n")
            else:
                file.write(f"{ip} | {server} | {code} | {host}\n")

    def save_and_print_hosts(hosts_dict, server_name, color):
        if hosts_dict:
            print(f"\n{color}# {server_name}\n")
            output_lines = [f"\n# {server_name}\n"]

            for host, ips in hosts_dict.items():
                if not cidr_mode and not is_ip_address(host):
                    print(f"{host}")
                    output_lines.append(host)
                
            if not cidr_mode:
                output_lines.extend('\r')
                all_ips = sorted(set(ip for ips in hosts_dict.values() for ip in ips))
                output_lines.extend(all_ips)
                print("\n" + "\n".join(all_ips))

            with open('/sdcard/CF.txt', 'a') as file:
                file.write("\n" + "\n".join(output_lines) + "\n")

    save_and_print_hosts(cloudfront_hosts, "CloudFront", c)
    print(f'\n{r}_____________________________________________________________\n')
    save_and_print_hosts(cloudflare_hosts, "Cloudflare", g)
    print(f'\n{r}_____________________________________________________________\n')

def disable_wake_lock():
    subprocess.run(['termux-wake-unlock'])

def parse_arguments():
    parser = argparse.ArgumentParser(description='HTTP Scanning Script')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-c', '--cidr', nargs='+', help='CIDR/IP-Range one (127.0.0.0/24) or more then (127.0.0.0/24 104.0.0.0/24)')
    group.add_argument('-f', '--file', nargs='+', help='File Path one (/sdcard/scan.txt) or more then (/sdcard/scan1.txt /sdcard/scan2.txt)')
    parser.add_argument('-p', '--port', default='80', help='Specify the port(s) to scan, default is 80')
    parser.add_argument('-t', '--timeout', default=3, type=int, help='Input Timeout, Default is 3 sec.')
    parser.add_argument('-T', '--threads', default=64, type=int, help='Input Threads, Default is 64')
    parser.add_argument('-o', '--output', default='/sdcard/other_respond.txt', help='Input Output Path (But /sdcard/CF.txt Always Default), Default is /sdcard/other_respond.txt')

    return parser.parse_args()

def main():
    args = parse_arguments()
    hosts = []

    if args.cidr:
        for cidr in args.cidr:
            hosts.extend(get_hosts_from_cidr(cidr))
        is_ip_only_mode = True
        cidr_mode = True
    elif args.file:
        for file_path in args.file:
            if not os.path.isfile(file_path):
                exit(f"File {file_path} not found.")
            hosts.extend(get_hosts_from_file(file_path))
        is_ip_only_mode = any(is_ip_address(host) for host in hosts)
        cidr_mode = False

    if not hosts:
        raise ValueError('No valid hosts to scan.')

    ports = args.port.split(',')
    DEFAULT_TIMEOUT = args.timeout
    threads = args.threads
    output_file = args.output

    try:
        print(f"\n{lb}[ {pr}* {lb}] {c} Acquiring Wake Lock...\n")
        enable_wake_lock()
        perform_scan(hosts, ports, output_file, threads, is_ip_only_mode=is_ip_only_mode, cidr_mode=cidr_mode)
        print(f'\n🚩 {r}࿗ {rkj}Jai Shree Ram {r}࿗ 🚩\n     🛕🛕🙏🙏🙏🛕🛕\n')
    finally:
        print(f"\n{lb}[ {pr}* {lb}] {c} Releasing Wake Lock...\n")
        disable_wake_lock()

if __name__ == '__main__':
    main()
