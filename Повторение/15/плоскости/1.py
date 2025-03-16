# 7934

#(х — 3у < А) ∨ (у > 400) ∨ (x > 56)
def f(x,y):
    return  (x -3*y <a) or (y > 400) or (x >56)

for a in range(0,100):
    if all(f(x,y)==1 for x in range(0,80) for y in range(0,401)):
        print(a)