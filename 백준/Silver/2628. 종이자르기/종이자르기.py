W, H = map(int, input().split()) # 종이의 가로, 세로
N = int(input()) #칼로 잘라야하는 점선의 개수

hor = [0] #가로
ver = [0] #세로
for _ in range(N):
    # 가로면 0 세로면 1
    idx, num = map(int, input().split())
    if idx:
        ver.append(num)
    else:
        hor.append(num)
ver.append(W)
hor.append(H)

ver.sort()
hor.sort()

ans = []
for v in range(1, len(ver)):
    for h in range(1, len(hor)):
       ans.append((ver[v]-ver[v-1])*(hor[h]-hor[h-1]))

print(max(ans))