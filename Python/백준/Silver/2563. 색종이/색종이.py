N = int(input()) # 색종이의 수

arr = [[0] * 100 for _ in range(100)]

for _ in range(N): # 색종이를 붙인 위치
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

count = 0
for i in range(100):
    for j in range(100):
        if arr[i][j]:
            count += 1

print(count)