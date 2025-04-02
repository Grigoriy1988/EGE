def f(x,y,w,z):
    return int((x <= (y and not(z))) or w)
print(f"x\ty\tw\tz\tf")
for x in 0,1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                F = f(x,y,w,z)
                if F == 0:
                    print(f"{x}\t{y}\t{w}\t{z}\t{F}")
