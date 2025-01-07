N = int(input()) #참가자 수
size = []
size = list(map(int, input().split())) #티셔츠 사이즈별 신청자의 수
T, P = map(int, input().split()) #티셔츠 묶음 수, 펜 묶음 수

import math
Tnum = 0
for i in range(6):
  Tnum += math.ceil(size[i]/T)

print(Tnum)

Pnum = 0
Pnum= N//P

print(Pnum, N-P*Pnum)