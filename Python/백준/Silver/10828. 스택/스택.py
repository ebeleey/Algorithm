import sys

N = int(sys.stdin.readline()) # 명령의 수
stack = []
for _ in range(N):
    command = sys.stdin.readline().strip()

    if command[:4] == 'push':
        _, x = command.split()
        stack.append(int(x))
    elif command == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)