from ipaddress import *

ip_узла = "111.81.208.27"
ip_сети = '111.81.192.0'
for mask in range(33):
    net = ip_network(f'{ip_узла}/{mask}',0)
    if ip_сети in str(net):
        print(net, net.netmask)
