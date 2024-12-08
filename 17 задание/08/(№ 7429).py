n= [int(x) for x in open('input.txt')]
min_xx = min([x for x in n if 10<=x<=99 and x % sum(int(i) for i in str(x))==0])
n_output = [(n[i], n[i+1]) for i in range(0,len(n) - 1) if n[i] % min_xx == 0 or n[i+1]% min_xx == 0]
m_s = max(sum(x) for x in n_output)
print(len(n_output),m_s)