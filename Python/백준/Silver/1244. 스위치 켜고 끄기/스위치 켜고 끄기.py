N = int(input()) #스위치 수
switches = list(map(int, input().split()))
switches.insert(0, 0)

op = [1, 0]
M = int(input()) #학생 수
for _ in range(M):
    sex, num = map(int, input().split())

    if sex == 1: #남학생이면
        for idx in range(1, N+1):
            if idx % num == 0: # 스위치 번호가 자기가 받은 수의 배수이면,
                 switches[idx] = op[switches[idx]] # 그 스위치의 상태를 바꾼다.
    else: #여학생이면
        i = 1
        switches[num] = op[switches[num]]
        while 1 <= num - i and num + i <= N:
            if switches[num-i] != switches[num+i]:
                break
            else:
                switches[num-i] = op[switches[num-i]]
                switches[num+i] = op[switches[num+i]]
                i += 1


for i in range((N+1)//10+1):
    print(*switches[1+10*i:11+10*i])