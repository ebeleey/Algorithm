N = int(input())

queen = [0] * (N)
answer = 0

def backtracking(r):
    global answer

    # 종료 조건
    if (r == N):
        answer += 1
        return
    
    for c in range(N):
        queen[r] = c

        if check(r):
            backtracking(r + 1)

    
def check(r):
    for i in range(r):
        # 같은 열
        if queen[i] == queen[r]:
            return False

        # 대각선
        if abs(r - i) == abs(queen[r] - queen[i]):
            return False

    return True

backtracking(0)

print(answer)