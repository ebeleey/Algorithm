
A, B = map(int, input().split())

answer = 0

while True:

    if B == A:
        answer += 1
        break
    elif A > B:
        answer = -1
        break

    elif str(B)[-1] == '1':
        answer += 1
        B = B // 10
        continue

    elif B % 2 == 0:
        answer += 1
        B = B // 2
        continue

    else:
        answer = -1
        break



print(answer)