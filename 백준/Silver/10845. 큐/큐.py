import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()

for _ in range(N):
    command = sys.stdin.readline().strip()
    if command[:4] == 'push':
        _, x = command.split()
        queue.append(x)
    elif command == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
            
