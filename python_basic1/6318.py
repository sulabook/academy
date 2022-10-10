list1 = list('abcdef')
list2 = [i for i in range(6)]
dict1 = dict(zip(list1, list2))
for item in dict1.items():
    print(f'{item[0]}: {item[1]}')
