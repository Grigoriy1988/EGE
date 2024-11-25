from ipaddress import*
ip_1 = ip_address('154.63.206.129')
ip_2 = ip_address('154.63.100.75')
for mask in range(32,0,-1):
    net1= ip_network(f'{ip_1}/{mask}',0)
    net2 = ip_network(f'{ip_2}/{mask}', 0)
    if net1 == net2:
        k = 0
        for ip in net1:
            if f'{ip:b}'.count('1') % 2 == 0:
                k+=1
        print(k)