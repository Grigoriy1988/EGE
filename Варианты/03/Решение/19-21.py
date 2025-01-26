def game(s1, s2, step):
    if s1+s2 >= 181:
        return step % 2 == 0
    if step == 0:
        return  0
    h = [game(s1+4,s2,step-1),game(s1,s2+4,step-1),game(s1*3,s2,step-1),game(s1,s2*3,step-1)]
    return any(h) if (step - 1) % 2 == 0 else all(h)

'''
Укажите минимальное значение S, при котором Петя не может выиграть за один ход, но при любом ходе Пети 
Ваня может выиграть своим первым ходом.
'''
print('19)',[s2 for s2 in range(1, 156) if game(25, s2, 2)])

print('20)',[s2 for s2 in range(1, 156) if not game(25, s2, 1) and game(25, s2, 3)])

print('21)',[s2 for s2 in range(1, 156) if not game(25, s2, 2) and game(25, s2, 4)])
