n = int(input())
level = 0

if n: # 의견이 하나 이상 있다면
    p = int(n*0.15+0.5)
    arr = [int(input()) for _ in range(n)]
    arr.sort()

    level = int(sum(arr[p:n-p])/(n-2*p)+0.5)

else: #난이도 의견이 없으면 0
    level = 0

print(level)