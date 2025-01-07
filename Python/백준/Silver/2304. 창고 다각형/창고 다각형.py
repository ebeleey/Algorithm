N = int(input()) #기둥의 개수

M = 1001
pillar = [0]*M

max_pillar = 0
max_idx = 0
for _ in range(N):
    l, h = map(int, input().split())
    pillar[l] = h
    if h > max_pillar:
        max_pillar = h
        max_idx = l

for i in range(max_idx):
    if pillar[i] > pillar[i+1]:
        pillar[i+1] = pillar[i]
for i in range(M-1, max_idx, -1):
    if pillar[i] > pillar[i-1]:
        pillar[i-1] = pillar[i]

print(sum(pillar))