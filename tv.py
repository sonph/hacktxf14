#!/usr/bin/env python3

import webbrowser as wb
import pdb

IP='192.168.1.19'
PORT='8080'
URL='hacktxf14.appspot.com'

def stop(ip):
    if ip is None:
        ip = IP
    url = 'http://%s:%s/itv/stopITV' % (IP, PORT)
    print('Executing %s' % url)
    wb.open_new_tab(url)

def start(url, ip):
    if ip is None:
        ip = IP
    if url is None:
        url = URL
    stop(ip)
    url = 'http://%s:%s/itv/startURL?url=http://%s/' % (ip, PORT, url)
    print('Executing %s' % url)
    wb.open_new_tab(url)

def printUsage():
    print('Usage: python tv.py [start|stop] [url] [ip]')
    print('Example:')
    print('    python tv.py start  # default hacktxf14.appspot.com')
    print('    python tv.py start hacktxf14.appspot.com')
    print('    python tv.py stop')

def main():
    import sys
    try:
        cmd = sys.argv[1]
        if cmd == 'start':
            url = sys.argv[2] if len(sys.argv) >= 3 else None
            if url is None:
                ip = sys.argv[2] if len(sys.argv) >= 3 else None
            else:
                ip = sys.argv[3] if len(sys.argv) >= 4 else None
            start(url, ip)
        elif cmd == 'stop':
            ip = sys.argv[2] if len(sys.argv) >= 3 else None
            stop(ip)
        else:
            printUsage()
    except:
        printUsage()
            
if __name__ == '__main__':
    main()
