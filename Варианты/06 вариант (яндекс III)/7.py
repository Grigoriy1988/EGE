k = 2
T = 44_000
i = 16
t = 60
paket = 32
v = 1_802_240  # бит/с
I = (k * T * i * t) * paket
tpaket = I / v
print(tpaket)

