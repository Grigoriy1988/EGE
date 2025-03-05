from ipaddress import *

ip_узла = "148.195.140.28"
ip_сети = '148.195.140.0'
for mask in range(33):
    net = ip_network(f'{ip_узла}/{mask}',0)
    if ip_сети in str(net):
        print(net, net.netmask,mask)