row, colm = map(int, input().split(', '))
result = [[0] * colm for _ in range(row)]
for i in range(row):
    for j in range(colm):
        result[i][j] = i * j
print(result)
