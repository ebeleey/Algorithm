# 터렛

T = int(input())


for tc in range(T):
    ans = 0 # 류재명이 있을 수 있는 위치의 수

    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = ((x1-x2)**2 + (y1-y2)**2)**(1/2)

    if x1==x2 and y1==y2: # 원의 중심이 같음
        if r1==r2: #반지름도 같음
            ans = -1
        else: # 반지름이 다름
            ans = 0
    elif d == (r1+r2) or d == abs(r1-r2):
        ans = 1
    elif abs(r1-r2)< d < (r1+r2):
        ans = 2
    else:
        ans = 0




    print(ans)