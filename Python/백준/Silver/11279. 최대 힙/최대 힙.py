from heapq import heappush, heappop
import sys

N = int(sys.stdin.readline()) # 연산의 개수
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x > 0: # 자연수
        heappush(heap, -x)
    else: # x==0
        if len(heap) == 0:
            print(0)
            continue
        k = heappop(heap)
        print(-k)