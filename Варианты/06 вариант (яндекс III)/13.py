from ipaddress import *
ip_net = '172.30.0.0'
mask = '255.254.0.0'
net = ip_network(f'{ip_net}/{mask}')
count = 0
for ip in net:
    ip_bit = f'{ip:b}'
    if ip_bit.count('1')%12 !=0:
        print(ip,ip_bit)
        count +=1
print(count)