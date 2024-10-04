# 𝑎 ∧ 𝑏 ∧ ¬𝑐 ∨ ¬𝑎 ∧ 𝑏 ∧ 𝑐 ∧ ¬𝑑 ∨ 𝑎 ∧ ¬𝑏 ∧¬𝑐 ∧ d
print(f"a\tb\tc\td\tf")
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                f = (a and b and not c) or (not a and b and c and not d) or (a and not b and not c and d)
                f = int(f)
                if f:
                    print(f"{a}\t{b}\t{c}\t{d}\t{f}")
