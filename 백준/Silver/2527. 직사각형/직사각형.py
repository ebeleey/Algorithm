for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    if (p1 < x2) or (p2 < x1) or (q1 < y2) or (q2 < y1):
        print("d") # 공통부분이 없음
    elif (x1 == p2 and y1 == q2) or (p1 == x2 and y1 == q2) or\
            (x1 == p2 and q1 == y2) or (p1 == x2 and q1 == y2):
        print("c") # 점
    elif (p1 == x2 and (y2 < q1 and y1 < q2)) or \
         (p2 == x1 and (y1 < q2 and y2 < q1)) or \
         (q1 == y2 and (x2 < p1 and x1 < p2)) or \
         (q2 == y1 and (x1 < p2 and x2 < p1)):
        print("b") # 선분
    else: # 직사각형
        print("a")

