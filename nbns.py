#scapy.sendrecv.send() 
from scapy.layers.l2 import ARP
from scapy.layers.netbios import NBNSQueryRequest
from scapy.layers.inet import IP,UDP
from scapy.packet import Raw
from scapy.sendrecv import sr1
import re

def getHostNameByIp(ip):
       packet=IP(dst=ip)/UDP(sport=137,dport=137)/NBNSQueryRequest(NAME_TRN_ID=0xc535, QUESTION_NAME= '*' + "\x00" * 14,QUESTION_TYPE=33,FLAGS=0x0000,ARCOUNT=0,QUESTION_CLASS=1)
       answer=sr1(packet,iface="Realtek PCIe GbE Family Controller",timeout=0.3,verbose=False)
       if answer==None:
              return "None"
       if answer.haslayer(Raw):
              s=str(answer[Raw])
              groups=re.search(r"b'\\x00\\x00\\x00\\x00\\x00e\\x03(.*)","".join(s.split(" ")[0]))
              return(groups.group(1))
       return "unknown"

