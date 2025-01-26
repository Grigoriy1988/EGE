from ipaddress import *
mask = '255.248.0.0'
ip_сети = '10.112.0.0'
net= ip_network(f'{ip_сети}/{mask}')
count = 0
for ip in net:
    ipbit = f'{ip:b}'
    if ipbit.count('1')%3==0:
        count+=1
        # print(ipbit)

print(count)