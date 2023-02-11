#!/bin/python3


import  sys
import socket
from datetime import datetime

#define target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # this will translate host name to ipv4.
# took a method of length and compared it with the input,argv is the amount of arguments and we need two arguments  
else:
		print("Invalid amount of argument")
		print("Input arguments as per below given syntax")
		print("Synatx: python3 crapy_port_scanner.py <ip_address>")

#adding a pretty banner
print("-" * 50)
print("Scanning target: "+target)
print("Time started: " +str(datetime.now()))

#making the script do something


try:
		for port in range(50,90):
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				socket.setdefaulttimeout(1)
				result = s.connect_ex((target,port)) #error indicator
				if result == 0: #that means the port is open  
					 print(f"port {port} is open")
				s.close()

except KeyboardInterrupt:
	print("\n Exiting Program......")
	sys.exit()

except socket.gaierror:
	print("could not resolve the hostname")
	sys.exit()

except socket.error:
	print("Could not connect to the server")
	sys.exit()


















