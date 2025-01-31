def game(s, step):
    if s <= 15:
        return step % 2 == 0
    if step == 0:
        return 0
    h = []
    while len(h) == 0:
        for k in range(2, 10):
            if s % k == 0:
                h.append(game(s - k, step - 1))
        if len(h) == 0:
            s -= 1
    return any(h) if (step - 1) % 2 == 0 else all(h)


'''
  Вопрос 1. Найдите минимальное значение S, при котором Ваня выигрывает своим первым ходом при любой игре Пети.
'''
print('19)', [s for s in range(16, 36) if game(s, 2)])
print('20)', [s for s in range(16, 36) if game(s, 3) and not game(s,1)])
print('21)', [s for s in range(16, 36) if game(s, 4) and not game(s,2)])