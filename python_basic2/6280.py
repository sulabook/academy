num = int(input())
result = list()

for i in range(1, num // 2 + 1):
    if num % i == 0:
        result.append(i)
result.append(num)
print(result)
