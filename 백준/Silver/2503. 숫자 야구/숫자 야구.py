from itertools import permutations

N = int(input())  # 민혁이가 영수에게 한 질문의 갯수
cases = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

for _ in range(N):
    q, s, b = input().split()  # 질문한 세자리 수, 스트라이크 개수, 볼의 개수
    q = list(map(int, q)) 
    s = int(s)
    b = int(b)

    new_cases = []

    for case in cases:
        strike_cnt = 0
        ball_cnt = 0

        for i in range(3):
            if case[i] == q[i]: # 스트라이크
                strike_cnt += 1  
            elif case[i] in q: # 볼
                ball_cnt += 1  

        if strike_cnt == s and ball_cnt == b:
            new_cases.append(case)

    cases = new_cases

print(len(cases))
