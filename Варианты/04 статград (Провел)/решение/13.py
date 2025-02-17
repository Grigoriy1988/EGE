from ipaddress import *

ip_узла = '68.30.20.70'
count = 0
for mask in range(1, 33):
    net = ip_network(f'{ip_узла}/{mask}', 0)
    if f'{net[0]:b}'.count('1') == f'{net.netmask:b}'.count('0'):
        print(net, net.netmask)
        for ip in net:
            if f'{ip:b}'.count('1') == 10:
                print(ip)
                count += 1
print(count)

