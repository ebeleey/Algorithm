import sys
sys.setrecursionlimit(100000)

nums = []

while True:
    try:
        nums.append(int(input()))
    except:
        break

root = 0 # 0번째 수가 루트

left = [-1] * len(nums)
right = [-1] * len(nums)

for i in range(1, len(nums)):
    
    cur = 0
    while True:

        if nums[i] < nums[cur]:
            if left[cur] == -1:
                left[cur] = i
                break
            cur = left[cur]
            
        else:
            if right[cur] == -1:
                right[cur] = i
                break
            cur = right[cur]
    

def post(idx):
    if idx == -1:
        return
    post(left[idx])
    post(right[idx])
    print(nums[idx])

post(root)