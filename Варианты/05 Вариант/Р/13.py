from ipaddress import *
mask = '255.255.240.0'
ip_узла = '228.172.236.0'
count = 0
net = ip_network(f'{ip_узла}/{mask}',0)
for ip in net:
    if f"{ip:b}".count('1') % 5 !=0:
        count+=1
print(count)