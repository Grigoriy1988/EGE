from ipaddress import *
ip_узла1 = ip_address("61.58.73.42")
ip_узла2 = ip_address('61.58.75.136')
for mask in range(32,0,-1):
    net1 = ip_network(f'{ip_узла1}/{mask}', 0)
    net2 = ip_network(f'{ip_узла2}/{mask}', 0)
    if net1 == net2 and (net1[0] <ip_узла1 < net1[-1]) and (net1[0] <ip_узла2< net1[-1]):
        print(mask)
        k = 0
        t = 0
        for ip in net1:
            s = '.'.join(f'{int(x):>08b}' for x in str(ip).split('.'))
            if s.count('1')%2!=0 and ip != net1[0] and ip != net1[-1]:
                t+=1
            print(f'{k}: {ip} {t}')
            k+=1
        break
print(t)