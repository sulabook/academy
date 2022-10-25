result= [1, 1]
[result.append(result[i - 1] + result[i - 2]) for i in range(2, 10)]
print(result)
