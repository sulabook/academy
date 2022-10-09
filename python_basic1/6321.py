import math

def _isprime(num):
    divisor = 1
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            divisor = i
    if divisor != 1:
        print('소수가 아닙니다.')
    else:
        print('소수입니다.')

_isprime(int(input()))
