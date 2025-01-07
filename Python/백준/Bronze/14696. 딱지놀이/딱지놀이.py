N = int(input()) #딱지놀이 총 라운드 수

for _ in range(N):
    a, *a_cards = map(int, input().split())
    b, *b_cards = map(int, input().split())

    a_counts = [0] * 5
    b_counts = [0] * 5

    for card in a_cards:
        a_counts[card] += 1
    for card in b_cards:
        b_counts[card] += 1

    if a_counts[4] > b_counts[4]:
        print("A")
    elif a_counts[4] < b_counts[4]:
        print("B")
    else: #비기면
        if a_counts[3] > b_counts[3]:
            print("A")
        elif a_counts[3] < b_counts[3]:
            print("B")
        else: #비기면
            if a_counts[2] > b_counts[2]:
                print("A")
            elif a_counts[2] < b_counts[2]:
                print("B")
            else: #비기면
                if a_counts[1] > b_counts[1]:
                    print("A")
                elif a_counts[1] < b_counts[1]:
                    print("B")
                else:
                    print("D")
