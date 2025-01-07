import sys

def binary_search_start(num):
    left = 0
    right = N-1
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == num:
            if mid == 0 or cards[mid-1] != num:
                return mid
            else:
                right = mid - 1
        elif num < cards[mid]:
            right = mid - 1
        elif num > cards[mid]:
            left = mid + 1
    return 0

def binary_search_end(num):
    left = 0
    right = N-1
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == num:
            if mid == N-1 or cards[mid+1] != num:
                return mid + 1
            else:
                left = mid + 1
        elif num < cards[mid]:
            right = mid - 1
        elif num > cards[mid]:
            left = mid + 1

    return 0

N = int(sys.stdin.readline()) # 상근이가 가지고 있는 숫자 카드의 개수
cards = list(map(int, sys.stdin.readline().split())) # 숫자 카드에 적혀있는 정수
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split())) # 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M 개의 정수

cards.sort()

ans = [0] * M
for i in range(M):
    s = binary_search_start(nums[i])
    e = binary_search_end(nums[i])

    ans[i] = e-s
print(*ans)