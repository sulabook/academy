num = int(input())
answer = ''

while num / 2 != 0: 
    answer = str(num % 2) + answer
    num //= 2

print(answer)
