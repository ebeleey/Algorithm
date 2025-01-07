M = 1234567891
r = 31

L = int(input()) # 문자열의 길이
chars = input() # 문자열

H = 0

for i in range(L):
    H += ((ord(chars[i])-96)*(r ** i))
print(H%M)