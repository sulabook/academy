num = input()
digitCnt = [0]*10

for digit in num:
    digitCnt[int(digit)] += 1

for i in range(10):
    if i == 9:
        print(f'{i}')
    else:
        print(f'{i}', end =' ')

for i in range(10):
    if i == 9:
        print(f'{digitCnt[i]}')
    else:
        print(f'{digitCnt[i]}', end =' ')
