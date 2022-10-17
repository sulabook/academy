list1 = [12,24,35,24,88,120,155,88,120,155]
result = []
[result.append(e) for e in list1 if e not in result]
print(result)
