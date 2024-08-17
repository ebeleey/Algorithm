N = int(input())

nums = [int(input()) for _ in range(N)]
nums.sort()

ans = 0

# 두 개의 최소값을 처리할 수 있을 때까지 반복
while len(nums) > 1:
    # 가장 작은 두 요소를 꺼내서 합침
    first = nums.pop(0)
    second = nums.pop(0)
    
    temp = first + second
    ans += temp
    
    # 새로운 합친 값을 정렬된 위치에 삽입
    # 리스트를 한 번 정렬하여 최적화된 삽입 정렬을 수행
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < temp:
            left = mid + 1
        else:
            right = mid
    nums.insert(left, temp)

print(ans)