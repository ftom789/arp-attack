from scapy.all import *

packets=sniff(filter="ip.addr==192.168.0.189&&nbns",timeout=10)