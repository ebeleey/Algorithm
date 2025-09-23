L, C = map(int, input().split()) # L: 암호의 길이, C: 주어지는 문자의 개수
letters = sorted(list(input().split()))

def make_password(password, moeum_cnt, idx):
    if len(password) == L and moeum_cnt >= 1 and L - moeum_cnt >= 2: # 암호 길이가 되면
        print(password)
        return

    for idx in range(idx, C):
        # print(letters[idx])
        if letters[idx] in {'a', 'e', 'i', 'o', 'u'}:
            make_password(password + letters[idx], moeum_cnt + 1, idx + 1)
        else:
            make_password(password + letters[idx], moeum_cnt, idx + 1)

make_password('', 0, 0)

