
# S 배열에 의해 카드를 섞는 함수
def shuffle(arr):
    new_arr = [0] * N

    for i in range(N):
        new_arr[S[i]] = arr[i]
    return new_arr

# P 배열에 의해 최종으로 와야하는 카드가 맞는지 확인하는 함수
def check(arr):
    for pos in range(N):
        if arr[pos] != pos % 3:
            return False
    return True

# 입력 받기
N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

cards = P[:]

start = cards[:]

ans = 0
while True:
    # 종료 조건(P 배열이랑 현재 카드 배열이 같으면)
    if check(cards):
        print(ans)
        break

    if ans > 0 and cards == start:
        print(-1)
        break

    # 다르면 섞는다
    cards = shuffle(cards)
    ans += 1