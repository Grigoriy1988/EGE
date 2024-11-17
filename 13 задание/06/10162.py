from ipaddress import *

ip_узла1 = "112.117.107.70"
ip_узла2 = '112.117.121.80'

for mask in range(33):
    net1 = ip_network(f'{ip_узла1}/{mask}',0)
    net2 = ip_network(f'{ip_узла2}/{mask}', 0)
    if net1 == net2:
        print(net1, net1.netmask,mask)

