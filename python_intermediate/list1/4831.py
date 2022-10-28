# T: total try
T = int(input())

for t in range(T):

    # K: 충전후 최대 이동 가능한 정류장 수
    # N: 0 ~ N 정류장
    # M: 충전기가 있는 정류장 수
    K, N, M = map(int, input().split(' '))

    # chargers: 충전기가 있는 정류장 위치
    chargers = list(map(int, input().split(' ')))

    # 충전기가 있는 정류장 위치를 고려한 0 ~ N 정류장
    busStops = [1 if i in chargers else 0 for i in range(N + 1)]

    # 모든 경우의 수
    routes = [busStops[:] for _ in range(2 ** M)]

    for i in range(2 ** M):     # 각각의 경우에서
        for j in range(1, M + 1):       # 충전기 위치에 0 / 1 분기를 만든다
            if (i // (2 ** (M - j))) % 2 == 0:      
                routes[i][chargers[j - 1]] = 0
            else:
                routes[i][chargers[j - 1]] = 1

    # 모든 경우를 순회하며 최소값을 찾음
    min_charge = M + 1      # 충전기수보다 1 큼. 종점 도착하는 경우 무조건 바뀜
    for route in routes:
        k = K       # 충전량
        i = 0       # 위치

        while k > 0 and i < N:      
            i += 1      # 위치 1 증가
            if i == N:      # 종점 도착 시
                if min_charge > sum(route):     # 값이 작으면 저장
                    min_charge = sum(route)
            k -= 1      # 충전량 1 감소
            if route[i] == 1:       # 충전기 있는 정류장이면 충전
                k = K

    if min_charge == M + 1:     # 도착하지 못하는 경우
        print(f'#{t + 1} 0')        # 0 출력
    else:
        print(f'#{t + 1} {min_charge}')
