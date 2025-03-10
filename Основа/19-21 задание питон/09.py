def game(s1, s2, step):
    if s1+s2 >= 227:
        return step % 2 == 0
    if step == 0:
        return  0
    h = [game(s1+1,s2,step-1),game(s1,s2+1,step-1),game(s1*2,s2,step-1),game(s1,s2*2,step-1)]
    return any(h) if (step - 1) % 2 == 0 else all(h)
'''
В начальный момент в первой куче было 17 камней, во второй куче – S камней; 1 ≤ S ≤ 209
'''
'''
Вопрос 1. Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети. Укажите минимальное значение S, при котором такая ситуация возможна.
'''
print('19)',[s2 for s2 in range(1, 210) if game(17, s2, 2)]) # поменять all на any

'''
Вопрос 2. Найдите два наименьших значения S, когда Петя имеет выигрышную стратегию, причём одновременно выполняются два условия:
− Петя не может выиграть за один ход;
− Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
'''
print('20)',[s2 for s2 in range(1, 210) if game(17, s2, 3) and not game(17,s2,1)])
'''
Вопрос 3. Найдите минимальное значение S, при котором одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
Спрятать ответ
'''
print('21)',[s2 for s2 in range(1, 210) if game(17, s2, 4) and not game(17,s2,2)])