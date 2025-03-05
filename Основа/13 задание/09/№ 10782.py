from ipaddress import*


ip_узла1 = ip_address('118.187.59.255')
ip_узла2 = ip_address('118.187.65.115')
for mask in range(31):
    net_1 = ip_network(f'{ip_узла1}/{mask}',0)
    net_2 = ip_network(f'{ip_узла2}/{mask}',0)
    if net_1 != net_2 and (net_1[0] <ip_узла1 < net_1[-1]) and (net_2[0] <ip_узла2 < net_2[-1]):
        print(net_1.netmask, net_1,net_2)

