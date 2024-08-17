def solution(N, stages):
    answer = []
    counts = [[0]*2 for _ in range(N+2)]

    for stage in stages:
        counts[stage][0] += 1
        for i in range(1, stage+1):
            counts[i][1] += 1
    print(counts)
    per = [[0]*2 for _ in range(N)]
    for i in range(1, N+1):
        per[i-1][0] = i
        if counts[i][1]:
            per[i-1][1] = counts[i][0] / counts[i][1]
        else:
            per[i-1][1] = 0

    per.sort(key= lambda x: -x[1])

    answer = [x[0] for x in per]
    # for item in per:
    #     answer.append(item[0])

    return answer

