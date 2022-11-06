# -*- coding: utf-8 -*-

T = int(input())        # 시도 횟수
for t in range(1, T + 1):
    K, N, M = map(int, input().split(' '))      # 최대 충전량, 정류장 수, 충전소 수
    C = list(map(int, input().split(' ')))      # 충전소 위치

    p = 0       # 현재 위치
    cnt = 0     # 충전 횟수
    past_c = -1     # 지난 충전소 인덱스
    flag = True        # 다음 충전소or 종점 도착 가능 여부

    while flag:
        # 현 위치에서 종점에 도착 가능한 경우
        if p + K >= N:
            break
    
        flag = False        # 충전소 들리면 True

        # 갈 수 있는 충전소 중 가장 멀리는 있는 충전소 확인
        for next_c in range(past_c + 1, len(C)):
            if p + K >= C[next_c]:
                past_c = next_c
                flag = True
            else:       # 도달할 수 없는 충전소에서 반복문 끝냄
                break

        # 충전소를 들릴 수 없는 경우flag = False인 채 break
        if not flag:       
            break

        p = C[past_c]       # 갈 수 있는 가장 먼 충전소로 현재 위치 이동
        cnt += 1        # 충전 횟수 1 증가
    
    print(f'#{t} {cnt}') if flag else print(f'#{t} 0')
