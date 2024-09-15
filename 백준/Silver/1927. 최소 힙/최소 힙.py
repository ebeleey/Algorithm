from heapq import heappop, heappush

import sys

N = int(sys.stdin.readline()) #연산의 개수
heap = []

for _ in range(N):
    x = int(sys.stdin.readline()) # 연산정보

    if x:
        heappush(heap, x)
    else: # 0
        if heap:
            print(heappop(heap))
        else:
            print(0)