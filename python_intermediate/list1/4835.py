T = int(input())

for t in range(T):
    N, M = map(int, input().split(' '))
    data_list = list(map(int, input().split(' ')))
    min_sum = 1e8
    max_sum = 1
    for i in range(N - M + 1):
        sumM = 0
        for j in range(M):
            sumM += data_list[i + j]
        if sumM < min_sum:
            print('min_sum = %s -> %s' % (min_sum, sumM))
            min_sum = sumM
        if sumM > max_sum:
            print('max_sum = %s -> %s' % (max_sum, sumM))
            max_sum = sumM
    print(f'#{t + 1} {max_sum - min_sum}')
