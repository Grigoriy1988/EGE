from ipaddress import *

ip_узла = "76.155.48.2"
ip_сети = '76.155.48.0'
count = 0
for mask in range(33):
    net = ip_network(f'{ip_узла}/{mask}',0)
    if ip_сети in str(net):
        print(net, net.netmask)
        count +=1
print(count)