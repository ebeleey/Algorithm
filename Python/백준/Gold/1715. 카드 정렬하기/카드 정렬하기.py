
N = int(input())

nums = [int(input()) for _ in range(N)]
nums.sort()

ans = 0
while len(nums) > 1:
    first = nums.pop(0)
    second = nums.pop(0)

    temp = first + second
    # temp = nums.pop(0) + nums.pop(0)
    ans += temp

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < temp:
            left = mid + 1
        else:
            right = mid
    nums.insert(left, temp)

print(ans)