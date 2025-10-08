N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort() # 정렬
visited = [False] * N

def func(arr):
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(N):
            if not visited[i]:
                visited[i] = True
                func(arr + [nums[i]])
                visited[i] = False

func([])