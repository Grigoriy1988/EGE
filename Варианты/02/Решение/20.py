def game(s, step):
    if s >= 30:
        return step % 2 == 0

    if step == 0:
        return 0
    h = [game(s + 1, step - 1),  game(s+3, step - 1),game(s*2, step - 1)]
    return any(h) if (step - 1) % 2 == 0 else all(h)

'''
Укажи, сколько существует значений S, при которых Петя выиграет своим первым ходом.
'''
print('20)', [s for s in range(1,30) if game(s,3) and not game(s,1)])

