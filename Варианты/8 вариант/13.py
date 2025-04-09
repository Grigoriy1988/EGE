from ipaddress import *
ip_сети = '148.195.140.0'
mask = '255.255.252.0'
net = ip_network(f'{ip_сети}/{mask}')
count = 0
for ip in net:
    if (ip != net[0] and ip != net[-1]):
        if f'{ip:b}'[:16].count('1')<=f'{ip:b}'[16:].count('0') and f'{ip:b}'[16:].count('0') % 2 !=0 :
            count +=1
            # print(ip)
print(count)
# f'{ip:b}'[:16].count('0')



from ipaddress import *
ip_сети = '112.154.132.0'
mask = '255.255.252.0'
net = ip_network(f'{ip_сети}/{mask}',0)
count = 0
for ip in net.hosts():
    if (ip != net[0] and ip != net[-1]):
        if f'{ip:b}'[:16].count('1')<=f'{ip:b}'[16:].count('0') and f'{ip:b}'[16:].count('0') % 2 !=0 :
            count +=1
            # print(ip)
print(count)