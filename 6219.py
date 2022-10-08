import math
num = int(input())
factors = []
for i in range(1, math.floor(math.sqrt(num)) + 1):
    if num % i == 0:
        print(f'{i}(은)는 {num}의 약수입니다.')
        factors.append(i)
print(f'{num}(은)는 {num}의 약수입니다.')
if len(factors) == 1:
    print(f'{num}(은)는 {factors[0]}과 {num}로만 나눌 수 있는 소수입니다.')
