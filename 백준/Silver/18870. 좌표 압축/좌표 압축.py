N = int(input())
nums = list(map(int, input().split()))

for i in range(N):
    nums[i] = [nums[i], i] # [값, 인덱스]

nums.sort()

prevnum = nums[0][0]
val = 0
nums[0][0] = val

for i in range(1, N):
    presnum = nums[i][0]
    if nums[i][0] == prevnum:
        nums[i][0] = val
    else:
        val += 1
        nums[i][0] = val
    prevnum = presnum
    
nums.sort(key = lambda x: x[1])

for i in range(N):
    print(nums[i][0], end = ' ')