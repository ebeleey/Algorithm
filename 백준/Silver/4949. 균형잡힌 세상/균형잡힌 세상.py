while True:
    chars = input()
    if chars == ".":
        break

    answer = "yes"
    stack = []
    for char in chars:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                answer = "no"
                break
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                answer = "no"
                break
    else:
        if stack:
            answer = "no"
    print(answer)