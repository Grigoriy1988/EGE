from ipaddress import*
mask = '255.255.255.192'
k= 0
for A in range(256):
    ip_узла = ip_address(f'207.0.{A}.167')
    net = ip_network(f'{ip_узла}/{mask}',0)
    if all(f'{ip:b}'[:16].count('0') > f'{ip:b}'[16:].count('0')for ip in net) and net[0]< ip_узла < net[-1]:
        print(A)
        k+=1
print(k)

