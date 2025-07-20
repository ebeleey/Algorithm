N = int(input())
M = int(input()) # 문자열의 길이
chars = input()

P = 'IO'* N + 'I'
cnt = 0

for i in range(M-N):
    if chars[i:i+2*N+1] == P:
        cnt += 1

print(cnt)