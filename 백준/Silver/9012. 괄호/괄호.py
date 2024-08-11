import sys

T = int(sys.stdin.readline())

for tc in range(1, T+1):
    chars = sys.stdin.readline()
    answer = "YES"
    stack = []
    for char in chars:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                answer = "NO"
                break
    else:
        if stack:
            answer = "NO"


    print(answer)