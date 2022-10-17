nums = list(map(int, input().split(', ')))
result = [str(num) for num in nums if num % 2 != 0]
print(', '.join(result))
