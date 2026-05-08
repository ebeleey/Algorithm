def solution(s):
    answer = -1
    stack = []
    
    for item in s:
        if stack and stack[-1] == item:
            stack.pop()
        else:
            stack.append(item)
            
    if stack:
        answer = 0
    else:
        answer = 1
    return answer