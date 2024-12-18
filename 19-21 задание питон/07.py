def game(s1, s2, step):
    if s1 == s2:
        return step % 2 == 0
    if step == 0:
        return 0
    h = [game(s1 + 1, s2, step - 1), game(s1 + 3, s2, step - 1)] if s1 < s2 else [game(s1, s2 + 1, step - 1),
                                                                                  game(s1, s2 + 3, step - 1)]
    return any(h) if (step - 1) % 2 == 0 else all(h)
s1 = 13
print('19)', [s2 for s2 in range(1,24) if game(s1,s2,2) and not s2 == s1])
print('20', [s2 for s2 in range(1,24) if game(s1,s2,3) and not (game(s1,s2,1)) and not s1==s2])
print('21', [s2 for s2 in range(1,24) if game(s1,s2,4) and not (game(s1,s2,2)) and not s1==s2])