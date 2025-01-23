from ipaddress import*
mask = ip_address('255.255.255.240')
ip_сети = ip_address('192.168.76.160')
net = ip_network(f'{ip_сети}/{mask}')
num = 0
cont = 0
for IP in net:
    a = bin(int(str(IP).split('.')[3]))[2:]
    if num % 2 == 0 and a.count('1') % 2 == 0 and IP != net[0]and IP != net[-1]:
        cont +=1
    num +=1
print(cont)




