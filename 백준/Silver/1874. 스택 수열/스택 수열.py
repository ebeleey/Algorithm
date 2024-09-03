
import sys
n = int(sys.stdin.readline()) # 1부터 n까지의 수
arr =  [int(sys.stdin.readline()) for _ in range(n)]


def func(n):

    stack = []
    idx = 0
    answer = []

    for i in range(1, n+1):
        stack.append(i)
        answer.append('+')
        if idx == n-1 and arr[idx] != stack[-1]:
            return ['NO']

        while len(stack) > 0 and idx < n and arr[idx] == stack[-1]:
            stack.pop()
            idx += 1
            # print('-')
            # print(stack)
            answer.append('-')
            # if idx == n - 1 or arr[idx] != stack[-1]:
            #     return ['NO']
    if len(stack):
        return ['NO']
    else:
        return answer

print(*func(n), sep='\n', end ='')