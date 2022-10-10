def _product(*nums):
    p = 1
    for num in nums:
        if type(num) is not int:
            return 'e'
        p *= num
    return p

p = _product(1, 2, '4', 3)
if p == 'e':
    print('에러발생')
else:
    print(p)
