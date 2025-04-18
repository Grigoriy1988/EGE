def game(s, step):
    if s == 42:
        return step % 2 == 0
    if s > 42:
        return step % 2 == 1

    if step == 0:
        return 0
    h = [game(s + 1, step - 1),  game(s +3, step - 1),  game(s +7, step - 1)]
    return any(h) if (step - 1) % 2 == 0 else all(h)


'''
  Вопрос 1. Укажите такое значение S, при котором Петя не может выиграть за один ход, но при любом ходе Пети Ваня может выиграть своим первым ходом.
'''
print('19)', [s for s in range(0,42) if game(s,2)])

'''
  Вопрос 2. Найдите два наименьших значения S, при которых у Пети есть выигрышная стратегия, причём Петя не может выиграть за один ход, но может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
'''
print('20', [s for s in range(0,42) if game(s,3) and (not game(s,1))])

'''
  Вопрос 3. Найдите минимальное значение S, при котором Ваня может выиграть первым или вторым ходом при любой игре Пети, но у него нет стратегии, которая позволит ему гарантированно выиграть первым ходом. Если найдено несколько значений S, в ответе запишите минимальное из них.
'''
print('21', [s for s in range(0,42) if game(s,4) and (not game(s,2))])