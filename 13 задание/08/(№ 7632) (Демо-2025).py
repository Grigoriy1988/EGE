from ipaddress import *

ip_сети = "172.16.168.0"
mask = '255.255.248.0'
k = 0
net = ip_network(f'{ip_сети}/{mask}')
for ip in net:
    print(ip)
    s = '.'.join(f'{int(x):>08b}' for x in str(ip).split('.'))
    if s.count('1') % 5 != 0:
        k += 1
    #print('.'.join(f'{int(x):>08b}' for x in str(ip).split('.')))  # перевод ip адреса
print(k)

