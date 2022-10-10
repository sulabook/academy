def _fibonacci(num):
    if num <= 0:
        return

    list1 = [0] * num
    list1[0] = n1 = 1
    list1[1] = n2 = 1

    if num >= 3:
        for i in range(2, num):
            list1[i] = n1 + n2
            n2 = n1
            n1 = list1[i]

    return list1[:num]

print(_fibonacci(10))
