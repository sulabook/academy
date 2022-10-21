T = int(input())
data = list()
for i in range(T):
    N = input()
    data.append(list(map(int, input().split(' '))))
for i in range(T):
    print(f'#{i + 1} {max(data[i]) - min(data[i])}')
