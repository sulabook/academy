import math
digit = int(input())
n = math.floor(math.sqrt(digit))

for i in range(1, n+1):
    if digit % i == 0:
        print(f'{i}(은)는 {digit}의 약수입니다.')
print(f'{digit}(은)는 {digit}의 약수입니다.')
