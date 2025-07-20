N = int(input())
M = int(input()) # 문자열의 길이
chars = input()

cnt = 0
cur = 0

for i in range(M):
    if cur % 2 == 0:
        temp = 'I'
    else:
        temp = 'O'

    if chars[i] == temp:
        cur += 1

        if cur == 2 * N + 1:
            cnt += 1
            cur = 2*N - 1

    else:
        if chars[i] == 'I':
            cur = 1
        else:
            cur = 0

print(cnt)

