from  ipaddress import *
ip_сети = '144.168.32.160'
maska = '255.255.255.240'
net = ip_network(f"{ip_сети}/{maska}")
count= 0
for ip in net:
    ip_bit = f'{ip:b}'

    if ip!= net[0] and ip!=net[-1] and ip_bit.count('1')% 2 == 0:
        print(ip_bit, ip)
        count +=1

print(count)