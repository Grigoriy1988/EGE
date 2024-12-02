for a in range(1,50):
    for b in range(1,50):
        for c in range(1,50):
            s = f'>{'2'*b}{'1'*a}{"3"*c}'
            while '>1' in s or '>2' in s or '>3' in s:
                if '>1' in s:
                    s = s.replace('>1', "21>3")
                if '>2' in s:
                    s = s.replace('>2', "32>")
                if '>3' in s:
                    s = s.replace('>3', "11>2")

            if s.count('1') ==71 and s.count('2') == 54 and s.count('3')==37:
                print(a,b,c)



