N, M = map(int, input().split()) # 아이들의 수 N, 놀이기구의 수 M
durations = list(map(int, input().split())) # 놀이기구의 운행 시간

# 시간 t분이 지났을 때 몇 명이 탔는지
# total = M명 + sum(t // durations[i] for i in range(M))

# total이 N이 될 때를 찾으면 됨
if N <= M:
    print(N)
    
else:
    left = 0
    right = 6e10

    while left <= right:
        mid = (left + right) // 2
        total = M + sum(mid // duration for duration in durations)

        if total >= N:
            t = mid
            right = mid - 1
        else:
            left = mid + 1

    temp_cnt = M + sum((t- 1) // duration for duration in durations)

    for i, d in enumerate(durations):
        if t % d == 0:
            temp_cnt += 1
            if temp_cnt == N:
                print(i + 1)
                break
