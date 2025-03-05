from ipaddress import*
ip_узла = ip_address('152.65.245.132')
for mask in range(16,25):
    net = ip_network(f'{ip_узла}/{mask}',0)
    if all(f'{ip:b}'[:16].count('0')>=f'{ip:b}'[16:].count('0') for ip in net) and net[0] < ip_узла < net[-1]:
        print(mask,net.netmask)