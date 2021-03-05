from scapy.layers.inet import IP,UDP
from scapy.layers.dns import DNS,DNSQR
from scapy.sendrecv import sr1

def getHostNameByIp(ip):
	pack=IP(dst="224.0.0.251")/UDP(sport=5353,dport=5353)/DNS(id=0,qr=0,opcode=0,qd=DNSQR(qname=f"{'.'.join(ip.split('.')[-1::-1])}.in-addr.arpa",qtype=12))
	an=sr1(pack,iface="Realtek PCIe GbE Family Controller",verbose=False,timeout=0.4)
	#an.show()
	if (an==None):
		return ("None")
	if (an.src==ip):
		return (an[DNS].an.rdata.decode())
	return ("unknown")
