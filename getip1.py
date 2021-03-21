# th3Scann3r
import socket
from datetime import datetime

hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
print(hostname, ipaddr)
file = open('myip.txt', 'w')
file.write(ipaddr)
file.close()
ipsplit = ipaddr.split(".")
# a = '{0}.{1}.{2}.0/24'.format(ipsplit[0], ipsplit[1], ipsplit[2])
# print(a)
ipsplit2 = ipsplit[0] + '.' + ipsplit[1] + '.' + ipsplit[3] + '.'
stn1 = 1
edn1 = 2
td1 = datetime.now()
print("scan has been initiated on", td1)


def scan(addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect((addr, 80))
    if result == 0:
       return 0
    else:
       return 1


def run1():
    for ip in range(stn1, edn1):
        addr = ipsplit2 + str(ip)
        if scan((addr)):
            print(addr, "this address is live")


run1()
td2 = datetime.now()
total = td2 - td1
print("scanning completed in", total)

file = open('hostname_ip.txt', 'w')
file.write(hostname + ' ' + ipaddr)
file.close()
# Passing the input 'a'
