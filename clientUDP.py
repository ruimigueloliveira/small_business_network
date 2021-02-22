import socket
import signal
import sys
import time
import psutil

def signal_handler(sig, frame):
	print('\nDone!')
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit...')

##

ip_addr = "127.0.0.1"
udp_port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	time.sleep(2)
	a = dict(psutil.virtual_memory()._asdict())
	b = a.get("percent")
	message = psutil.cpu_percent()
	sock.sendto(str(message).encode(), (ip_addr, udp_port))
	sock.sendto(str(b).encode(), (ip_addr, udp_port))
