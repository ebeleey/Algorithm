# 집합
import sys
M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    command = sys.stdin.readline().split()
    if command[0] == 'all': # S를 {1, 2, ..., 20} 으로 바꾼다.
        S = set(range(1, 21))
    elif command[0] == 'empty': # S를 공집합으로 바꾼다.
        S.clear()
    else:
        X = int(command[1])
        if command[0] == 'add': # S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
            S.add(X)
        elif command[0] == 'remove': # S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
            if X in S:
                S.remove(X)
        elif command[0] == 'toggle': # S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
            if X in S:
                S.remove(X)
            else:
                S.add(X)
        elif command[0] == 'check': # S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
            if X in S:
                print(1)
            else:
                print(0)
