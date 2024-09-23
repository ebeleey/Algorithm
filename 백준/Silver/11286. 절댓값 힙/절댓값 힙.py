import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline()) # 연산의 개수
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())

    if x > 0:
        heappush(heap, [x, 1])
    elif x < 0:
        heappush(heap, [-x, -1])
    else: # x == 0
        if len(heap) == 0:
            print(0)
            continue
        num, sign = heappop(heap)
        print(num*sign)
