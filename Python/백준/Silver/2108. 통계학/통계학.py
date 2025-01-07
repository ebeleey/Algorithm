N = int(input())
arr = [int(input()) for _ in range(N)]

# 산술평균
print(round(sum(arr)/N))

# 중앙값
arr.sort()
print(arr[N//2])

# 최빈값
setarr = list(set(arr))
countarr = [[] for _ in range(len(setarr))]
setarr.sort()
for i in range(len(setarr)):
    countarr[i] = [setarr[i], 0]

for item in arr:
    for i in range(len(countarr)):
        if item == countarr[i][0]:
            countarr[i][1] += 1
            break

countarr.sort(key=lambda x: x[1])

if len(countarr) == 1:
    print(countarr[0][0])
elif countarr[-1][1] == countarr[-2][1]:
    countarr.sort(key = lambda x: (x[1], -x[0]))
    print(countarr[-2][0])
else:
    print(countarr[-1][0])


# 범위
print(arr[-1]-arr[0])