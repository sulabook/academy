result = [0] * 8

for i in range(2, 10):
    result[i - 2]  = list()
    for j in range(1, 10):
        if i * j % 3 == 0 or i * j % 7 == 0:
            continue
        else:
            result[i - 2].append(i * j)

print(result)
