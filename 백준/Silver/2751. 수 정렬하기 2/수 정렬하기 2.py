import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]

arr.sort()

for x in arr:
    print(x)