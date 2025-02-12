f = open('24.txt').readline()
f = f.replace('SQRP', '****')
f = f.replace('*SQR', '****')
f = f.replace('*SQ', '***')
f = f.replace('*S', '**')
f = f.replace('QRP*', '****')
f = f.replace('RP*', '***')
f = f.replace('P*', '**')
f = f.replace('S', ' ').replace('Q', ' ').replace('R', ' ').replace('P', ' ')
f = f.split()
print(max(len(i) for i in f))
# Второй способ
f = open('24.txt').readline()
for i in range(1, 100):
    if 'SQRP' * i in f:
        print(i, len('SQRP' * i))
    else:
        break
print("P" + 'SQRP' * 12 in f)
print("P" + 'SQRP' * 12 + "SQR" in f)
print(len("P" + 'SQRP' * 12 + "SQR"))
