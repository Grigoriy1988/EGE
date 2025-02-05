for A in range(0, 100):
    if all((x <= 19) or (y < 2 * x + A - 50) or (y > 17) for x in range(-5, 100) for y in range(-5, 100)):
        print(A)
