f = open('26.txt')
N = int(f.readline())
matrix = dict()
for _ in range(N):
    line, column = map(int, f.readline().split())
    if line in matrix:
        matrix[line].add(column)
    else:
        matrix[line] = {column}
max_point = [0,0]
for key, val in matrix.items():
    line = sorted(val)
    if len(line) == 1:
        m = 1
    elif len(line) == 2:
        m = 2 if line[1] - line[0]-1 > 500 else 0
    else:
        m = line[1]-line[0]-1>500
        m+=line[-1]-line[-2]-1>500
        for i in range(1, len(line) - 1):
            m+=(line[i+1]-line[i]-1>500) and (line[i]-line[i-1]-1>500)
    if m >max_point[0] or m == max_point[0] and key > max_point[1]:
        max_point = [m,key]
print(max_point)
