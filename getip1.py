#th3Scann3r
import socket
hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
print(hostname , ipaddr)
file = open('myip.txt', 'w')
file.write(ipaddr)
file.close()
ipsplit = ipaddr.split(".")
a = '{0}.{1}.{2}.0/24'.format(ipsplit[0], ipsplit[1], ipsplit[2])
print(a)
file = open('hostname_ip.txt', 'w')
file.write(hostname+ ' ' + ipaddr)
file.close()
# Passing the input 'a'

