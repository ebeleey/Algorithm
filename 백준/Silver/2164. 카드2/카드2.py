from collections import deque

N = int(input()) # N장의 카드
q = deque(list(range(1, N+1)))
qlen = N

while qlen > 1:
    q.popleft()
    qlen -= 1
    if qlen == 1:
        break
    q.append(q.popleft())

print(q[0])