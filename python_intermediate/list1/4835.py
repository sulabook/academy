T = int(input())

for t in range(T):
    N, M = map(int, input().split(' '))
    data_list = list(map(int, input().split(' ')))
    sum_list = [0] * (N - M + 1)
    for i in range(N - M + 1):
        for j in range(M):
            sum_list[i] += data_list[i + j]
    min_sum = min(sum_list)
    max_sum = max(sum_list)
    print(f'#{t + 1} {max_sum - min_sum}')
