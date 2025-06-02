N, M, B = map(int, input().split()) 

grounds = [list(map(int, input().split())) for _ in range(N)]

answer = []
for h in range(257):
    excess = 0
    shortage = 0

    for i in range(N):
        for j in range(M):
            if grounds[i][j] > h: # 이 칸이 평평하게 만드려는 높이보다 높다면
                excess += grounds[i][j] - h # 초과하는 걸 깎아야 함
            if grounds[i][j] < h: # 이 칸이 평평하게 만드려는 높이보다 낮다면
                shortage += h - grounds[i][j] # 부족한 걸 메꿔야 함
    
    if shortage <= B + excess: # 내가 갖고 있는 블럭이 부족한 블럭보다 같거나 많으면
        answer.append([excess * 2 + shortage, h])

answer.sort(key=lambda x: (x[0], -x[1]))
print(*answer[0])