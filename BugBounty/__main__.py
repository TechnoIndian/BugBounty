import argparse
import sys

from .Bug_Bounty import BugBounty

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
