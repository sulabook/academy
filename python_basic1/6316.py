list1 = [i for i in range(1, 11)]
print(list(map(lambda x: x * x, (filter(lambda x: x % 2 == 0, list1)))))
