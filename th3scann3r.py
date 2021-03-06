# th3Scann3r
import socket
import networkscan
import os
from datetime import datetime

#For Windows environment#

hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
#print(hostname, ipaddr)

#For Linux environment#

#gw = os.popen("ip -4 route show default").read().split()
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.connect((gw[2], 0))
#ipaddr = s.getsockname()[0]
#gateway = gw[2]
#host = socket.gethostname()
#print("IP:", ipaddr, " GW:", gateway, " Host:", host)

file = open('myip.txt', 'w')
file.write(ipaddr)
file.close()
ipsplit = ipaddr.split(".")
a = '{0}.{1}.{2}.0/24'.format(ipsplit[0], ipsplit[1], ipsplit[2])
#print(a)
print("-------th3scann3r--------")
td1 = datetime.now()
print("scan is initiated on", td1)

if __name__ == '__main__':
    my_scan = networkscan.Networkscan(a)
    print("netowrk to scan: " + str(my_scan.network))
    print("prefix to scan: " + str(my_scan.network.prefixlen))
    print("number of host to scan: " + str(my_scan.nbr_host))
    my_scan.run()
    for b in my_scan.list_of_hosts_found:
        print(b)

td2 = datetime.now()
total = td2 - td1
print("scanning completed in", total)
