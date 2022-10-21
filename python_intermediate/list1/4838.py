T = int(input())
data = list()
for i in range(T):
    N = input()
    data.append(input().split(' '))
for i in range(T):
    print(f'#{i + 1} {int(max(data[i])) - int(min(data[i]))}')
