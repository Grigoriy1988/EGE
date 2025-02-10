a = int(input())
b = int(input())
d = int(input())
ra = a % d if a % d < d - a % d else d - a % d
rb = b % d if b % d < d - b % d else d - b % d

if ra > rb:
    print(b)
elif ra < rb:
    print(a)
elif a < b:
    print(a)
else:
    print(b)
