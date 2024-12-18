def game(k, s, step):
    if k + s >= 45:
        return step % 2 == 0
    if step == 0:
        return 0
    h = [game(k + 2, s, step - 1), game(k, s + 2, step - 1), game(k * 3, s, step - 1), game(k, s * 3, step - 1)]
    return any(h) if (step - 1) % 2 == 0 else all(h)


print('19', len([(k, s) for k in range(1, 44) for s in range(1, 44) if k + s <= 43 and game(k, s, 2)]))
print('20', [s for s in range(1, 44) if 4 + s <= 43 and game(4, s, 3) and not game(4, s, 1)])
print('21', [s for s in range(1, 44) if 13 + s <= 43 and game(13, s, 4) and not game(13, s, 2)])