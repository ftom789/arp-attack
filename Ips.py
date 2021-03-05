import subprocess
import re
import nbns
import mdns
# from scapy.sendrecv import sr
# from scapy.layers.l2 import ARP
# from scapy.layers.netbios import NBNSRequest
# from scapy.layers.inet import UDP,IP,Ether
def getGateway():
    s=subprocess.run('ipconfig | findstr /i "Gateway"', shell=True,capture_output=True,text=True).stdout
    s=re.search("Default Gateway . . . . . . . . . : (.*)",s)
    return (s.group(1))


import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def getAllIps(choice=-1):
    s=subprocess.run(f"arp /a /n {get_ip()}",capture_output=True,text=True).stdout
    arp =((s.split("\n")[3:-1]))
    arp[0]+= " gateway"
    arp[0]=str(1)+f") {arp[0]}"
    
        
    for i in range(1,len(arp)):
        ip=arp[i].split(' ')[2]
        if choice==-1:
            hostname=nbns.getHostNameByIp(ip)
            if(hostname =="unknown" or hostname=="None"):
                hostname=mdns.getHostNameByIp(ip)
            arp[i]=str(i+1)+f") {arp[i]} {hostname}"
    
    
    if choice==-1:
        print("num      IP                        MAC       static/dynamic  NAME")
        print("\n".join(arp))
        choice=int(input("choose ip from the list: "))
        choice-=1
    groups=re.search("(.*)   (.*)         (.*)     (.*)   ",arp[choice])
    return ((groups.group(2).replace(" ",""),groups.group(3)))



