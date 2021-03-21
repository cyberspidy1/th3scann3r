# th3Scann3r -- cyberspidy
import socket
import networkscan
from datetime import datetime

hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
print(hostname, ipaddr)
file = open('myip.txt', 'w')
file.write(ipaddr)
file.close()
ipsplit = ipaddr.split(".")
a = '{0}.{1}.{2}.0/24'.format(ipsplit[0], ipsplit[1], ipsplit[2])
print(a)
td1 = datetime.now()
print("scan is initiated on", td1)

if __name__ == '__main__':
    network = a
    my_scan = networkscan.Networkscan(network)
    my_scan.run()
    for i in my_scan.list_of_hosts_found:
        print(i)

td2 = datetime.now()
total = td2 - td1
print("scanning completed in", total)

file = open('hostname_ip.txt', 'w')
file.write(hostname + ' ' + ipaddr)
file.close()

